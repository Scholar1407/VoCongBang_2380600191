from flask import Flask, request, jsonify

from cipher.rsa.rsa_cipher import RSACipher

app = Flask(__name__)

# RSA
rsa_cipher = RSACipher()

@app.route('/api/rsa/generate_keys', methods=['GET'])
def generate_keys():
    rsa_cipher.generate_keys()
    
    return jsonify({"message": "RSA Keys generated successfully!"})

@app.route('/api/rsa/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    message = data.get("message", "")
    key_type = data.get("key_type")

    if key_type == "public":
        key = rsa_cipher.load_keys()["public_key"]
    elif key_type == "private":
        key = rsa_cipher.load_keys()["private_key"]
    else:
        return jsonify({"error": "Invalid key type"})
    
    encrypted_message = rsa_cipher.encrypt(message, key)
    encrypted_hex = encrypted_message.hex()
    
    return jsonify({"encrypted_message": encrypted_hex})

@app.route('/api/rsa/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    ciphertext_hex = data.get("ciphertext")
    key_type = data.get("key_type")
    key = rsa_cipher.load_keys()["public_key"] if key_type == "public" else rsa_cipher.load_keys()["private_key"]
    ciphertext = bytes.fromhex(ciphertext_hex)
    decrypted_message = rsa_cipher.decrypt(ciphertext, key)

    return jsonify({"decrypted_message": decrypted_message})

@app.route('/api/rsa/sign', methods=['POST'])
def sign():
    data = request.json
    message = data.get("message", "")
    private_key = rsa_cipher.load_keys()["private_key"]
    signature_hex = rsa_cipher.sign(message, private_key).hex()

    return jsonify({"signature": signature_hex})

@app.route('/api/rsa/verify', methods=['POST'])
def verify():
    data = request.json 
    message = data.get("message", "")
    signature_hex = data.get("signature", "")
    public_key = rsa_cipher.load_keys()["public_key"]
    signature = bytes.fromhex(signature_hex)
    is_verified = rsa_cipher.verify(message, signature, public_key)

    return jsonify({"is_verified": is_verified})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)