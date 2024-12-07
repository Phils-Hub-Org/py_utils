from cryptography.fernet import Fernet

def decryptData(data: bytes, key: bytes) -> bytes:
    """ Decrypts data using Fernet decryption. """
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(data)
    return decrypted_data

if __name__ == '__main__':
    encrypted_data = b'gAAAAABnJLYfpBqTCcbFBDCXdMGwnBopG0OS69TXtGYI8PuS0BquhJANyTa24Cu5SU-fH4sBCzF02R2rXFxVK1jzbwBP7P8thg=='  # b'Phil81334'
    key = b'2onj-QH6-Gdc5Q1xjC58ap1CNN0e6hFxXXiSOVmioJ4='

    decrypted_data = decryptData(encrypted_data, key)
    print(decrypted_data)  # b'Phil81334'