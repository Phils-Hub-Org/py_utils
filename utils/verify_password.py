import bcrypt

def verifyPassword(non_hashed_str: str, hashed_str: str) -> bool:
    if not isinstance(non_hashed_str, str) or not isinstance(hashed_str, str):
        raise TypeError('Both inputs must be strings')
    
    return bcrypt.checkpw(non_hashed_str.encode('utf-8'), hashed_str.encode('utf-8'))

if __name__ == '__main__':
    print(
        verifyPassword(
            non_hashed_str='password',
            hashed_str='$2b$12$o/Qu4MpK0P7Qgi8wNArEf.L7YguV1Q2iWERRZT4UIuc0sB9VPsb5e'
        )
    )