from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher

app = Flask(__name__)

# Khởi tạo các đối tượng thuật toán
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()

# ==========================================
# CAESAR CIPHER ROUTES (Bài 2.5.1)
# ==========================================
@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.json
    plain_text = data.get('plain_text', '')
    key = int(data.get('key', 0))
    encrypted_message = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_message})

@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.json
    cipher_text = data.get('cipher_text', '')
    key = int(data.get('key', 0))
    decrypted_message = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_message})

# ==========================================
# VIGENERE CIPHER ROUTES (Bài 2.5.2)
# ==========================================
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data.get('plain_text', '')
    key = data.get('key', '')
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data.get('cipher_text', '')
    key = data.get('key', '')
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# Khởi chạy server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)