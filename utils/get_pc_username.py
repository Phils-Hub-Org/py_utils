import getpass

def getPcUsername() -> str:
    """ Returns the current username of the system. """
    return getpass.getuser()


if __name__ == '__main__':
    print(getPcUsername())  # Phil-