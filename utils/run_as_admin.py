import sys, ctypes

def runAsAdmin() -> bool:
    # Re-launch the script with admin privileges
    params = f'"{sys.executable}" "{__file__}"'
    result = ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, params, None, 1)
    return result > 32


if __name__ == '__main__':
    runAsAdmin()