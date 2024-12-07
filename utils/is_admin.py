import ctypes

def isAdmin() -> bool:
    return ctypes.windll.shell32.IsUserAnAdmin()

if __name__ == '__main__':
    print(isAdmin())  # 0