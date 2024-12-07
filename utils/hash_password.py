import bcrypt

def hashPassword(string) -> str:
    if not isinstance(string, str):
        raise TypeError('Input must be a string')
    
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(string.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

if __name__ == '__main__':
    print(hashPassword('password'))  # $2b$12$o/Qu4MpK0P7Qgi8wNArEf.L7YguV1Q2iWERRZT4UIuc0sB9VPsb5e