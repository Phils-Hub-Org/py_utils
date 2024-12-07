from typing import Callable

def verifyHashedString(non_hashed_str: str, hashed_str: str, hashString: Callable) -> bool:
    if not isinstance(non_hashed_str, str) or not isinstance(hashed_str, str):
        raise TypeError('Both inputs must be strings')
    
    return hashString(non_hashed_str) == hashed_str

if __name__ == '__main__':
    from hash_string import hashString
    print(verifyHashedString(
        non_hashed_str='password',
        hashed_str='b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86',
        hashString=hashString)
    )