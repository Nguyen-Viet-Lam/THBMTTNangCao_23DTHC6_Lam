from flask import Flask, request, jsonify
from cipher.caesar.caesar_cipher import CaesarCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher
from cipher.railfence.railfence_cipher import RailFenceCipher
from cipher.playfair.playfair_cipher import PlayFairCipher
app = Flask(__name__)

# Khởi tạo
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayFairCipher() # Thêm bài mới

# ... (Các route cũ giữ nguyên) ...

# PLAYFAIR ROUTES
@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.json
    key = data['key']
    matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({"playfair_matrix": matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def play_encrypt():
    data = request.json
    matrix = playfair_cipher.create_playfair_matrix(data['key'])
    return jsonify({'encrypted_text': playfair_cipher.playfair_encrypt(data['plain_text'], matrix)})

@app.route('/api/playfair/decrypt', methods=['POST'])
def play_decrypt():
    data = request.json
    matrix = playfair_cipher.create_playfair_matrix(data['key'])
    return jsonify({'decrypted_text': playfair_cipher.playfair_decrypt(data['cipher_text'], matrix)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)