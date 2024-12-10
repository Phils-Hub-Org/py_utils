import random
import string

def generateObfuscatedName(length) -> str:
    # Ensure the length by generating from 10^(length-1) to (10^length) - 1
    lower_bound = 10**(length - 1)
    upper_bound = (10**length) - 1
    random_int = random.randint(lower_bound, upper_bound)
    prefix = random.choice(string.ascii_uppercase)  # Random uppercase letter
    # prefix = random.choice(string.ascii_lowercase)  # Random lowercase letter
    return f'{prefix}{random_int}'

if __name__ == '__main__':
    print(generateObfuscatedName(15))