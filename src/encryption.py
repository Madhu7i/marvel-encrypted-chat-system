from Crypto.Cipher import AES
import base64

key = b'Sixteen byte key'  # Ensure this key is the same on both client and server

def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    return base64.b64encode(nonce + ciphertext).decode()

def decrypt_message(key, encrypted_message):
    raw_data = base64.b64decode(encrypted_message)
    nonce = raw_data[:16]
    ciphertext = raw_data[16:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt(ciphertext).decode()
