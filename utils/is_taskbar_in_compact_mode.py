import winreg

def isTaskbarInCompactMode():
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced', 0, winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, 'TaskbarSmallIcons')
        winreg.CloseKey(registry_key)
        return value == 1
    except FileNotFoundError:
        return False

if __name__ == '__main__':
    compact_mode = isTaskbarInCompactMode()
    if compact_mode:
        print('Taskbar is in compact mode (small icons).')
    else:
        print('Taskbar is not in compact mode.')