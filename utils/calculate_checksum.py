import os, hashlib

def calculateChecksum(file_path: str, buffer_size: int = 1024) -> str:
    """
    In your calculateChecksum function, you're generating a SHA-256 hash of the file content as a hexadecimal string using hash_sha256.hexdigest().
    Since this produces a deterministic output (i.e., the same file always generates the same hash), comparing two checksum values with == is a valid way to check if the files are identical.

    If checksum_val_1 == checksum_val_2, it means that both files (or data blocks) have the exact same content.
    If they differ, it means the files have different contents.
    """
    hash_sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(buffer_size), b''):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

if __name__ == '__main__':
    # data.text contents: "test"
    print(calculateChecksum(os.path.join(os.getcwd(), 'Misc', 'data.txt')))  # 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08