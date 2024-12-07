import sys

def isExecutable() -> bool:
    return getattr(sys, 'frozen', False)

if __name__ == '__main__':
    print(isExecutable())