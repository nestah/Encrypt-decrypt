from cryptography.fernet import Fernet
import os
import re

KEY_FILE = "secret.key"

def generate_key():
    return Fernet.generate_key()

def save_key(key):
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    print("Key saved to", KEY_FILE)

def load_key():
    if not os.path.exists(KEY_FILE):
        print("Key file not found. Generating a new key.")
        key = generate_key()
        save_key(key)
    else:
        print("Loading existing key from", KEY_FILE)
    return open(KEY_FILE, "rb").read()

def encrypt_reference_id(reference_id, key):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(reference_id.encode())
    return encrypted

def decrypt_reference_id(encrypted_reference_id, key):
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_reference_id).decode()
    return decrypted

def validate_reference_id(reference_id):
    # Define allowed special characters
    ALLOWED_SPECIAL_CHARACTERS = "!@#$%^&*"
    # Check if the length is at least 12
    if len(reference_id) < 12:
        return False
    # Regex pattern to match alphanumeric and allowed special characters
    pattern = f"^[a-zA-Z0-9{re.escape(ALLOWED_SPECIAL_CHARACTERS)}]+$"
    return re.match(pattern, reference_id) is not None
