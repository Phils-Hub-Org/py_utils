import os

def getAppDataRootDir() -> str:
    return os.path.join(os.path.join(os.path.expanduser('~'), 'Desktop'), 'AppData')

if __name__ == '__main__':
    print(getAppDataRootDir())  # C:\Users\Phil-\Desktop\AppData