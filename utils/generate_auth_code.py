import random

def generateAuthCode() -> str:
    # Generate a random 5-digit auth code
    return random.randint(10000, 99999)

if __name__ == '__main__':
    print(generateAuthCode())