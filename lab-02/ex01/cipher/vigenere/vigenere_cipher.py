class VigenereCipher:
    def __init__(self):
        pass
    
    def encrypt_text(self, plain_text, key):
        encrypt_text = ""
        key_index = 0

        for char in plain_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')
                if char.isupper():
                    encrypted_char = chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
                else:
                    encrypted_char = chr((ord(char) - ord('a') + key_shift) % 26 + ord('a'))
                key_index += 1
            else:
                encrypted_char += char
        
        return encrypt_text
    
    def decrypt_text(self, cipher_text, key):
        decrypt_text = ""
        key_index = 0

        for char in cipher_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')
                if char.isupper():
                    decrypted_char = chr((ord(char) - ord('A') - key_shift) % 26 + ord('A'))
                else:
                    decrypted_char = chr((ord(char) - ord('a') - key_shift) % 26 + ord('a'))
                key_index += 1
            else:
                decrypted_char += char
        
        return decrypt_text