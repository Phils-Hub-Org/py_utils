def decryptFile(file_path: str, key: bytes, decryptData: callable) -> bytes:
    """ Decrypts a file using Fernet decryption. """
    with open(file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    
    decrypted_data = decryptData(encrypted_data, key)

    return decrypted_data

if __name__ == '__main__':
    pass