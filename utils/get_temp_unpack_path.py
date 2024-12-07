import os, sys

def getTempUnpackPath(is_executable: bool) -> str:
    if not is_executable:
        print('Can only obtain this path when running as an executable')
        return
    # When running as an executable, PyInstaller unpacks embedded files into a temporary directory
    unpack_path = os.path.join(sys._MEIPASS)

    return unpack_path

if __name__ == '__main__':
    from is_executable import isExecutable
    getTempUnpackPath(isExecutable())