import os, sys

def getCurrProgramPath() -> str:
    """Return the absolute path of the current executable."""
    return os.path.abspath(sys.argv[0])

if __name__ == '__main__':
    print(getCurrProgramPath())  # c:\Users\Phil-\OneDrive\__Workbase_Backup__\Phils-Hub\Github\local_repos\py_utils\utils\get_current_program_path.py