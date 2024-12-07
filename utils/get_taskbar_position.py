# utils/get_taskbar_pos.py

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
ABE_LEFT = 0
ABE_TOP = 1
ABE_RIGHT = 2
ABE_BOTTOM = 3

def getTaskbarPosition():
    appbar_data = APPBARDATA()
    appbar_data.cbSize = ctypes.sizeof(APPBARDATA)
    
    result = ctypes.windll.shell32.SHAppBarMessage(ABM_GETTASKBARPOS, ctypes.byref(appbar_data))
    if result:
        if appbar_data.uEdge == ABE_LEFT:
            return 'left'
        elif appbar_data.uEdge == ABE_TOP:
            return 'top'
        elif appbar_data.uEdge == ABE_RIGHT:
            return 'right'
        elif appbar_data.uEdge == ABE_BOTTOM:
            return 'bottom'

    print('Failed to get taskbar position (SHAppBarMessage failed), defaulting to top')
    return 'top'

if __name__ == '__main__':
    position = getTaskbarPosition()
    print(f'Taskbar is at: {position}')
