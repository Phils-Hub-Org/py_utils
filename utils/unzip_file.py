import zipfile

def unzipFile(zip_file_path: str, extract_to: str) -> None:
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

if __name__ == '__main__':
    pass