import os, json, logging
from typing import Union, Callable

logger = logging.getLogger(__name__)

import json
from typing import Union

def readFromFile(file_path: str, is_bytes: bool = False, is_json: bool = False) -> Union[str, dict]:
    if is_json and is_bytes:
        raise ValueError("Cannot be both 'is_json' and 'is_bytes' at the same time.")
    
    with open(file_path, 'rb' if is_bytes else 'r') as f:
        if is_json:
            return json.loads(f.read())
        else:
            if is_bytes:
                return f.read().decode()
            return f.read()

def safeReadFromFile(
    file_path: str,
    is_bytes: bool = False,
    is_json: bool = False,
    slots: dict[str, Callable[[str], None]] = {
        'FileNotFoundError': lambda message: logger.error(message),
        'PermissionError': lambda message: logger.error(message),
        'IsADirectoryError': lambda message: logger.error(message),
        'OSError': lambda message: logger.error(message),
        'JSONDecodeError': lambda message: logger.error(message),
        'Exception': lambda message: logger.error(message),
        'finally': lambda message: logger.info(message),
    }
) -> None:
    # Default result variable is not needed anymore
    try:
        with open(file_path, 'rb' if is_bytes else 'r') as f:
            if is_json:
                return json.loads(f.read())  # Attempt to load JSON
            else:
                return f.read()  # Read raw bytes or text as appropriate
    except FileNotFoundError:
        if 'FileNotFoundError' in slots:
            slots['FileNotFoundError'](f"Error: The file '{file_path}' was not found.")
    except PermissionError:
        if 'PermissionError' in slots:
            slots['PermissionError'](f"Error: Permission denied when accessing '{file_path}'.")
    except IsADirectoryError:
        if 'IsADirectoryError' in slots:
            slots['IsADirectoryError'](f"Error: The path '{file_path}' is a directory, not a file.")
    except OSError as e:
        if 'OSError' in slots:
            slots['OSError'](f"OS error occurred: {e}")
    except json.JSONDecodeError:
        if 'JSONDecodeError' in slots:
            slots['JSONDecodeError'](f"Error: Failed to decode JSON from file '{file_path}'.")
    except Exception as e:
        if 'Exception' in slots:
            slots['Exception'](f"An unexpected error occurred while reading '{file_path}': {e}")
    finally:  # runs always, whether an exception was raised or not
        if 'finally' in slots:
            slots['finally']('Calling the finally slot.')

# Example Usage
if __name__ == '__main__':
    log_file_path = os.path.join(os.getcwd(), 'Logs', f'{os.path.basename(__file__)}.log')
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[logging.StreamHandler(), logging.FileHandler(log_file_path)]  # Add a file handler
    )

    print(safeReadFromFile(
        os.path.join(os.getcwd(), '--misc', 'file.json'),
        is_json=True
    ))

    print(safeReadFromFile(
        os.path.join(os.getcwd(), '--misc', 'file.txt'),
        slots={}  # No messages will be printed
    ))