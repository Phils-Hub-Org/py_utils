import os, sys

def restartExe(is_executable: bool) -> None:
    if not is_executable:
        print('Can only restart this program when running as an executable')
        return
    python = sys.executable
    os.execl(python, python, *sys.argv)

if __name__ == '__main__':
    from utils.is_executable import isExecutable
    restartExe(isExecutable())