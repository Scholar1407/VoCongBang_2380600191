from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12346))
server_socket.listen(5)

print("Generating DH parameters (this might take a few seconds)...")
parameters = dh.generate_parameters(generator=2, key_size=2048)
server_private_key = parameters.generate_private_key()
server_public_key = server_private_key.public_key()

pem_params = parameters.parameter_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.ParameterFormat.PKCS3
)
pem_public = server_public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

clients = []

def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    ciphertext = encrypted_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode()

def recvall(sock, n):
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data.extend(packet)
    return bytes(data)

def handle_client(client_socket, client_address):
    print(f"Client {client_address} connected.")
    aes_key = None
    
    try:
        # 1. Send DH parameters
        client_socket.sendall(len(pem_params).to_bytes(4, 'big'))
        client_socket.sendall(pem_params)
        
        # 2. Send Server Public Key
        client_socket.sendall(len(pem_public).to_bytes(4, 'big'))
        client_socket.sendall(pem_public)
        
        # 3. Receive Client Public Key
        client_pub_len_bytes = recvall(client_socket, 4)
        if not client_pub_len_bytes:
            raise ConnectionError("Failed to receive client public key length")
        client_pub_len = int.from_bytes(client_pub_len_bytes, 'big')
        
        pem_client_public = recvall(client_socket, client_pub_len)
        if not pem_client_public:
            raise ConnectionError("Failed to receive client public key")
            
        client_public_key = serialization.load_pem_public_key(pem_client_public)
        
        # 4. Compute shared secret
        shared_secret = server_private_key.exchange(client_public_key)
        
        # 5. Derive AES key (32 bytes)
        aes_key = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b'handshake data',
        ).derive(shared_secret)
        
        clients.append((client_socket, aes_key))
        
        while True:
            encrypted_message = client_socket.recv(2048)
            if not encrypted_message:
                break
            decrypted_message = decrypt_message(aes_key, encrypted_message)
            print(f"Received from {client_address}: {decrypted_message}")
            
            for client, key in clients:
                if client != client_socket:
                    encrypted = encrypt_message(key, decrypted_message)
                    client.sendall(encrypted)
            if decrypted_message.lower() == "exit":
                break
    except Exception as e:
        print(f"Error/Disconnect from client {client_address}: {e}")
            
    if aes_key and (client_socket, aes_key) in clients:
        clients.remove((client_socket, aes_key))
    client_socket.close()
    print(f"Client {client_address} disconnected.")

print("Server is listening on port 12346")
while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()