from flask import Flask, request, jsonify, render_template
import backend

app = Flask(__name__)
key = backend.load_key()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    reference_id = data.get('referenceId', '').strip()

    if backend.validate_reference_id(reference_id):
        encrypted_reference_id = backend.encrypt_reference_id(reference_id, key)
        return jsonify({'encryptedReferenceId': encrypted_reference_id.decode()})
    else:
        return jsonify({'error': 'Invalid Reference ID'}), 400

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    encrypted_reference_id = data.get('encryptedReferenceId', '')

    try:
        decrypted_reference_id = backend.decrypt_reference_id(encrypted_reference_id.encode(), key)
        return jsonify({'decryptedReferenceId': decrypted_reference_id})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
