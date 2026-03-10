from flask import Flask, request, jsonify
from cipher.caesar.caesar_cipher import CaesarCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher
# Sửa dòng dưới đây cho giống bài Vigenere lúc nãy:
from cipher.railfence.railfence_cipher import RailFenceCipher
app = Flask(__name__)

caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()

@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.json
    return jsonify({'encrypted_message': caesar_cipher.encrypt_text(data['plain_text'], int(data['key']))})

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    return jsonify({'encrypted_text': vigenere_cipher.vigenere_encrypt(data['plain_text'], data['key'])})

@app.route('/api/railfence/encrypt', methods=['POST'])
def rail_encrypt():
    data = request.json
    return jsonify({'encrypted_text': railfence_cipher.rail_fence_encrypt(data['plain_text'], int(data['key']))})

@app.route('/api/railfence/decrypt', methods=['POST'])
def rail_decrypt():
    data = request.json
    return jsonify({'decrypted_text': railfence_cipher.rail_fence_decrypt(data['cipher_text'], int(data['key']))})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)