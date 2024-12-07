from cryptography.fernet import Fernet

def encryptData(data: bytes, key: bytes) -> bytes:
    """
    Encrypts data using Fernet encryption.

    Note:
        Encrypting "phil" will always output the same value.
        There's no chance that diff inputs can have same outputs.
    """
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data)
    return encrypted_data

if __name__ == '__main__':
    # the following 3 all do the same thing.
    # utf-8 is the default encoding for strings, of which can be overridden.
    data = b'Phil81334'
    # data = bytes('Phil81334', 'utf-8')
    # data = 'Phil81334'.encode('utf-8')

    from generate_encryption_key import generateEncryptionKey
    key = generateEncryptionKey()
    print(key)  # b'2onj-QH6-Gdc5Q1xjC58ap1CNN0e6hFxXXiSOVmioJ4='

    encrypted_data = encryptData(data, key)
    print(encrypted_data)  # b'gAAAAABnJLYfpBqTCcbFBDCXdMGwnBopG0OS69TXtGYI8PuS0BquhJANyTa24Cu5SU-fH4sBCzF02R2rXFxVK1jzbwBP7P8thg=='