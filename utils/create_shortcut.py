import os
from win32com.client import Dispatch

def createShortcut(target: str, shortcut_dest: str, icon_path: str = None, args: str = None, start_in: str = None) -> None:
    """Create a shortcut to a target file with optional arguments and start-in path."""
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_dest)
    shortcut.TargetPath = target
    if args:
        shortcut.Arguments = args
    if icon_path:
        shortcut.IconLocation = icon_path
    if start_in:
        shortcut.WorkingDirectory = start_in  # Set the "Start In" directory
    shortcut.save()

if __name__ == '__main__':
    wawRootDir = r'D:\SteamLibrary\steamapps\common\Call of Duty World at War'
    modName = 'zm_test1'
    mapName = 'nazi_zombie_prototype'
    exeName = 'CoDWaW'
    wawArgs = rf'+set fs_game mods/{modName} +devmap {mapName} +set r_fullscreen 0'
    wawPath = rf'"{wawRootDir}\{exeName}.exe"'  # root + exe requires to be wrapped in double quotes

    newShortcutPath = os.path.expanduser(rf'~\Desktop\{modName}.lnk')  # store on users desktop
    iconPath = rf'{wawRootDir}\{exeName}.ico'
    if not os.path.exists(iconPath):
        iconPath = None
    startInPath = wawRootDir  # "Start In" path (working directory)

    createShortcut(
        target=wawPath,  # this is the "Target" Path (exe > properties > shorcut tab > target path field)
        shortcut_dest=newShortcutPath,  # store shortcut on the user's desktop
        icon_path=iconPath,  # Set icon
        args=wawArgs,  # set the target path args
        start_in=startInPath  # set the "Start In" path
    )