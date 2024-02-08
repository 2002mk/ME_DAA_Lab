from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def des_encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plaintext = pad(plaintext.encode('utf-8'), DES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def des_decrypt(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_data = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_data, DES.block_size).decode('utf-8')
    return plaintext

# Example usage:
key = get_random_bytes(8)  # 8 bytes key for DES
plaintext = input("enter the plain text:\n")

print("Original Message:", plaintext)

encrypted_msg = des_encrypt(key, plaintext)
print("Encrypted Message (in bytes):", encrypted_msg)

decrypted_msg = des_decrypt(key, encrypted_msg)
print("Decrypted Message:", decrypted_msg)