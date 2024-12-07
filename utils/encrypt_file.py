import os

def encryptFile(path_of_file_to_encrypt: str, encrypted_file_dir: str, encrypt_filename: str, key: bytes, encryptData: callable) -> None:
    """
    Encrypts a file using Fernet encryption.

    Args:
        path_of_file_to_encrypt (str): The path to the file to be encrypted.
        encrypted_file_dir (str): The directory to store the encrypted file.
        encrypt_filename (str): The name of the file to encrypt.
        key (bytes): The encryption key.
    """
    with open(path_of_file_to_encrypt, 'rb') as file:
        data = file.read()        

    encrypted_data = encryptData(data, key)

    with open(f"{os.path.join(encrypted_file_dir, encrypt_filename)}.encrypted", 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

if __name__ == '__main__':
    pass