import win32process, win32gui

def findWindowByPID(pid):
    """Find a window by its process ID."""
    hwnd = None
    def callback(hwnd, extra):
        _, window_pid = win32process.GetWindowThreadProcessId(hwnd)
        if window_pid == pid and win32gui.IsWindowVisible(hwnd):
            extra.append(hwnd)
    
    windows = []
    win32gui.EnumWindows(callback, windows)
    
    return windows[0] if windows else None