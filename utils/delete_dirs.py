import shutil

def delete_dirs(*dir_paths: str) -> None:
    """ Recursively deletes the specified directory/directories. """
    for dir_path in dir_paths:
        shutil.rmtree(dir_path)

if __name__ == '__main__':
    pass