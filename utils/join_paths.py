import os

MAX_PATH_LENGTH_WINDOWS = 260

def joinPaths(*components: str) -> str:
    """ Join multiple path components into a single path. """
    path:str = os.path.join(*components)

    # Check if a path is too long based on the maximum path length supported by the system.
    if len(path) > MAX_PATH_LENGTH_WINDOWS:
        if path.startswith('\\\\?\\'):
            return path
        else:
            # Join multiple path components into a single long path.
            return fr'\\?\{os.path.join(*components)}'
    else:
        return path

if __name__ == '__main__':
    print(joinPaths('D:', 'SteamLibrary', 'steamapps', 'common', 'Call of Duty World at War'))  # D:SteamLibrary\steamapps\common\Call of Duty World at War