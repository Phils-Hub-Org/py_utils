import os

def getMainDrive() -> str:
    """Returns the main drive of the system."""
    return os.getenv('SystemDrive')

if __name__ == '__main__':
    print(getMainDrive())  # C: