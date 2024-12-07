import platform

def getSysOs() -> str:
    return platform.system()

if __name__ == '__main__':
    print(getSysOs())  # Windows