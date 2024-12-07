import os, sys

def getCurrProgramName() -> str:
    """Return the name of the current executable."""
    return os.path.basename(sys.argv[0])

if __name__ == '__main__':
    print(getCurrProgramName())  # get_current_program_name.py