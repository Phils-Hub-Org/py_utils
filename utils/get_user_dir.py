import os

def getUserDir() -> str:
    """ Returns the user profile directory of the system. """
    return os.getenv('USERPROFILE')

if __name__ == '__main__':
    print(getUserDir())  # C:\Users\Phil-