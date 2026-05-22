from cipher.caesar import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET
    
    def encrypt_text(self, plain_text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        plain_text = plain_text.upper()
        encrypt_text = []
        
        for letter in plain_text:
            if letter in self.alphabet:
                letter_index = self.alphabet.index(letter)
                output_index = (letter_index + key) % alphabet_len
                output_letter = self.alphabet[output_index]
                encrypt_text.append(output_letter)
            else:
                encrypt_text.append(letter)
                
        return "".join(encrypt_text)

    def decrypt_text(self, cipher_text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        cipher_text = cipher_text.upper()
        decrypt_text = []
        
        for letter in cipher_text:
            if letter in self.alphabet:
                letter_index = self.alphabet.index(letter)
                output_index = (letter_index - key) % alphabet_len
                output_letter = self.alphabet[output_index]
                decrypt_text.append(output_letter)
            else:
                decrypt_text.append(letter)
        
        return "".join(decrypt_text)