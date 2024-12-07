import string, random

def generatePassword(length: int=12, include_special_chars: bool=True) -> str:
    chars = string.ascii_letters + string.digits
    if include_special_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == '__main__':
    print(generatePassword())  # \F.xwgu`Pf':