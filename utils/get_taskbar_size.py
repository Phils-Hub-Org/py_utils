# utils/get_taskbar_size.py

import ctypes
from ctypes import wintypes

class APPBARDATA(ctypes.Structure):
    _fields_ = [
        ('cbSize', ctypes.c_ulong),
        ('hWnd', wintypes.HWND),
        ('uCallbackMessage', ctypes.c_uint),
        ('uEdge', ctypes.c_uint),
        ('rc', wintypes.RECT),
        ('lParam', ctypes.c_long),
    ]

ABM_GETTASKBARPOS = 0x00000005

def getTaskbarSize():
    appbar_data = APPBARDATA()
    appbar_data.cbSize = ctypes.sizeof(APPBARDATA)
    
    result = ctypes.windll.shell32.SHAppBarMessage(ABM_GETTASKBARPOS, ctypes.byref(appbar_data))
    if result:
        # Print debug info about taskbar position
        print(f'Taskbar rect: left={appbar_data.rc.left}, top={appbar_data.rc.top}, '
              f'right={appbar_data.rc.right}, bottom={appbar_data.rc.bottom}')
        
        # Calculate taskbar height or width based on position
        if appbar_data.uEdge in (0, 2):  # Left or Right
            size = appbar_data.rc.right - appbar_data.rc.left  # Width
        elif appbar_data.uEdge in (1, 3):  # Top or Bottom
            size = appbar_data.rc.bottom - appbar_data.rc.top  # Height
        else:
            print(f'Unknown taskbar edge value: {appbar_data.uEdge}')
            return 30
        
        # ensure size is an integer
        if not isinstance(size, int):
            try:
                size = int(size)
            except ValueError:
                print(f'Invalid taskbar size detected: {size}')
                return 30
            
        # Sanity check the size
        if size <= 0 or size > 300:  # Taskbar shouldn't be larger than 300px
            print(f'Invalid taskbar size detected: {size}px')
            return 30
            
        return size

    print('Failed to get taskbar size (SHAppBarMessage failed), defaulting to 30px')
    return 30

if __name__ == '__main__':
    taskbar_size = getTaskbarSize()
    print(f'Taskbar size: {taskbar_size}px')
