from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from flask import Flask, jsonify, render_template, request
import socket
import threading
import webbrowser
import time

SERVER_HOST = "localhost"
SERVER_PORT = 12346
WEB_HOST = "127.0.0.1"
WEB_PORT_START = 5000

app = Flask(__name__)

client_socket = None
aes_key = None
connected = True
message_id = 0
incoming_messages = []
messages_lock = threading.Lock()
client_id = 1

def find_free_port(start=WEB_PORT_START):
    for port in range(start, start + 100):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe:
            try:
                probe.bind((WEB_HOST, port))
                return port
            except OSError:
                continue
    return start

def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

def decrypt_message(key, encrypted_message):
    iv = encrypted_message[: AES.block_size]
    ciphertext = encrypted_message[AES.block_size :]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode()

def add_incoming_message(text):
    global message_id
    with messages_lock:
        message_id += 1
        incoming_messages.append(
            {"id": message_id, "type": "received", "text": text}
        )

def recvall(sock, n):
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data.extend(packet)
    return bytes(data)

def connect_to_server():
    global client_socket, aes_key

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    # 1. Receive DH parameters
    param_len_bytes = recvall(client_socket, 4)
    if not param_len_bytes:
        raise ConnectionError("Failed to receive param length")
    param_len = int.from_bytes(param_len_bytes, 'big')
    pem_params = recvall(client_socket, param_len)
    parameters = serialization.load_pem_parameters(pem_params)
    
    # 2. Receive Server Public Key
    pub_len_bytes = recvall(client_socket, 4)
    pub_len = int.from_bytes(pub_len_bytes, 'big')
    pem_public = recvall(client_socket, pub_len)
    server_public_key = serialization.load_pem_public_key(pem_public)
    
    # 3. Generate Client Key Pair
    client_private_key = parameters.generate_private_key()
    client_public_key = client_private_key.public_key()
    pem_client_public = client_public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    # 4. Send Client Public Key
    client_socket.sendall(len(pem_client_public).to_bytes(4, 'big'))
    client_socket.sendall(pem_client_public)
    
    # 5. Compute shared secret & derive AES key
    shared_secret = client_private_key.exchange(server_public_key)
    aes_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'handshake data',
    ).derive(shared_secret)

def receive_messages():
    global connected

    while connected:
        try:
            encrypted_message = client_socket.recv(2048)
            if not encrypted_message:
                break

            decrypted_message = decrypt_message(aes_key, encrypted_message)
            add_incoming_message(decrypted_message)

            if decrypted_message.lower() == "exit":
                break
        except OSError:
            break

    connected = False
    try:
        client_socket.close()
    except OSError:
        pass

@app.route("/")
def index():
    return render_template("chat.html", client_id=client_id)

@app.route("/api/messages")
def get_messages():
    since = request.args.get("since", 0, type=int)

    with messages_lock:
        new_messages = [msg for msg in incoming_messages if msg["id"] > since]

    return jsonify({"connected": connected, "messages": new_messages})

@app.route("/api/send", methods=["POST"])
def send_message():
    global connected

    if not connected:
        return jsonify({"ok": False, "error": "disconnected"})

    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()
    if not message:
        return jsonify({"ok": False, "error": "empty message"})

    try:
        encrypted_message = encrypt_message(aes_key, message)
        client_socket.sendall(encrypted_message)

        if message.lower() == "exit":
            connected = False

        return jsonify({"ok": True})
    except OSError as exc:
        connected = False
        return jsonify({"ok": False, "error": str(exc)})

def open_browser(port):
    time.sleep(0.8)
    webbrowser.open(f"http://{WEB_HOST}:{port}")

def main():
    global client_id

    web_port = find_free_port()
    client_id = web_port - WEB_PORT_START + 1

    print("Connecting to server and performing Diffie-Hellman Key Exchange...")
    connect_to_server()

    receive_thread = threading.Thread(target=receive_messages, daemon=True)
    receive_thread.start()
    browser_thread = threading.Thread(
        target=open_browser, args=(web_port,), daemon=True
    )
    browser_thread.start()

    print(f"Connected to server {SERVER_HOST}:{SERVER_PORT}")
    print(f"Open browser at http://{WEB_HOST}:{web_port}")
    print("Type 'exit' in chat to quit.")

    app.run(host=WEB_HOST, port=web_port, debug=False, use_reloader=False)

if __name__ == "__main__":
    main()