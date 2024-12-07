from cryptography.fernet import Fernet

def generateEncryptionKey() -> bytes:
    """ Generates a Fernet encryption key. """
    return Fernet.generate_key()

if __name__ == '__main__':
    key = generateEncryptionKey()
    print(key)