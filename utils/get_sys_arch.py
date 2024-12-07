import platform

def getSysArch() -> str:
    return platform.machine()


if __name__ == '__main__':
    print(getSysArch())  # AMD64