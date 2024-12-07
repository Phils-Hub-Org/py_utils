# utils/write_to_file.py

import os, json, logging
from typing import Callable, Union

def writeToFile(file_path: str, content: Union[str, dict, bytes], is_bytes: bool = False, is_json: bool = False, mkdir: bool = False) -> None:
    # Ensure the directory exists
    if mkdir:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'wb' if is_bytes else 'w') as file:
        if is_json:
            json.dump(content, file, indent=4)  # Will raise TypeError if content is not serializable
        else:
            if is_bytes:
                file.write(content)
            else:
                file.write(str(content))