import os, subprocess
from typing import Union

def runExecutable(running_dir: str, exe_path: str, exe_args: str) -> Union[bool, str]:
    """
    Runs the given executable with no arguments.
    exe_path: Path to the executable file
    """

    os.chdir(running_dir)  # required

    try:
        subprocess.Popen(
            [exe_path, exe_args],
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
        return True, f"Successfully ran {exe_path}"
    except subprocess.CalledProcessError as e:
        return False, f"Error occurred while running {exe_path}: {e}"
    except FileNotFoundError:
        return False, f"Executable not found: {exe_path}"

if __name__ == '__main__':
    runExecutable(
        running_dir=r'D:\SteamLibrary\steamapps\common\Call of Duty World at War',
        exe_path=r'D:\SteamLibrary\steamapps\common\Call of Duty World at War\CoDWaW.exe',
        exe_args=r'+set fs_game mods/zm_test1 +devmap nazi_zombie_prototype +set r_fullscreen 0'
    )