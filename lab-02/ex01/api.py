from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher

app = Flask(__name__)

''' Caesar Cipher API '''
ceasar_cipher = CaesarCipher()

@app.route('/api/caesar/encrypt', methods=["POST"])
def caeser_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypt_text = ceasar_cipher.encrypt_text(plain_text, key)
    
    return jsonify({"encrypt_message": encrypt_text})

@app.route('/api/caesar/decrypt', methods=["POST"])
def caeser_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypt_text = ceasar_cipher.decrypt_text(cipher_text, key)
    
    return jsonify({"decrypt_message": decrypt_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    
    

''' Vigenere Cipher API '''
vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=["POST"])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypt_text = vigenere_cipher.encrypt_text(plain_text, key)
    
    return jsonify({"encrypt_message": encrypt_text})

@app.route('/api/vigenere/decrypt', methods=["POST"])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypt_text = vigenere_cipher.decrypt_text(cipher_text, key)
    
    return jsonify({"decrypt_message": decrypt_text})