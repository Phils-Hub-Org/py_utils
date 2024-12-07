import os, sys

def getProgramDir() -> str:
    return os.path.dirname(os.path.abspath(sys.argv[0]))

if __name__ == '__main__':
    print(getProgramDir())  # c:\Users\Phil-\OneDrive\__Workbase_Backup__\Phils-Hub\Github\local_repos\py_utils\utils