import ctypes, win32gui

def minimizeCmdWindow() -> None:
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd != 0:
        win32gui.ShowWindow(hwnd, 6)  # Minimize the window

if __name__ == '__main__':
    minimizeCmdWindow()