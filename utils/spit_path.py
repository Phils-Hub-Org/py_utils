import os

def splitPath(text: str) -> str:
    root, ext = os.path.splitext(text)
    return root, ext

if __name__ == "__main__":
    dir, filename = splitPath(r'C:\Users\user\Desktop\file.txt')
    print(dir)
    print(filename)