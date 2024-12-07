import os

def getDesktopDir() -> str:
    return os.path.join(os.path.expanduser('~'), 'Desktop')

if __name__ == '__main__':
    print(getDesktopDir())  # C:\Users\Phil-\Desktop