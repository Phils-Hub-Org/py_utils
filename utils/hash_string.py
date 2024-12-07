import hashlib

def hashString(string: str) -> str:
    if not isinstance(string, str):
        raise TypeError('Input must be a string')
    
    return hashlib.sha512(string.encode('utf-8')).hexdigest()

if __name__ == '__main__':
    hashed_string = hashString('password')  # b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86
    print(hashed_string)