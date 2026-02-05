from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

import os

# Function to generate AES key from password
def generate_key(password):
    salt = get_random_bytes(16)  # Random salt
    key = PBKDF2(password, salt, dkLen=32)  # PBKDF2 to derive 256-bit key
    return key, salt

# Encrypt the file using AES-256 in CBC mode
def encrypt_file(file_path, password):
    key, salt = generate_key(password)  # Generate the key and salt from password
    iv = get_random_bytes(AES.block_size)  # Random initialization vector

    cipher = AES.new(key, AES.MODE_CBC, iv)

    with open(file_path, 'rb') as file:
        data = file.read()

    encrypted_data = cipher.encrypt(pad(data, AES.block_size))

    # Save the salt, IV, and encrypted data to a new file
    encrypted_file_path = file_path + '.enc'
    with open(encrypted_file_path, 'wb') as enc_file:
        enc_file.write(salt + iv + encrypted_data)  # Save salt + IV + encrypted content

    return encrypted_file_path

# Decrypt the file using AES-256 in CBC mode
def decrypt_file(encrypted_file_path, password):
    with open(encrypted_file_path, 'rb') as enc_file:
        salt = enc_file.read(16)  # Extract salt
        iv = enc_file.read(AES.block_size)  # Extract IV
        encrypted_data = enc_file.read()  # The rest is the encrypted data

    # Derive the key from password and salt
    key = PBKDF2(password, salt, dkLen=32)

    cipher = AES.new(key, AES.MODE_CBC, iv)

    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    decrypted_file_path = encrypted_file_path.rstrip('.enc')  # Remove '.enc' from file name
    with open(decrypted_file_path, 'wb') as dec_file:
        dec_file.write(decrypted_data)

    return decrypted_file_path
