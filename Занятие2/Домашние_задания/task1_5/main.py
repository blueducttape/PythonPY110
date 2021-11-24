from string import ascii_lowercase, ascii_uppercase, digits
import random


def generate_password(n: int) -> str:
    small_letters = ascii_lowercase
    big_letters = ascii_uppercase
    symbols = small_letters + big_letters + digits
    password = random.choice(small_letters) + random.choice(big_letters) + random.choice(digits)
    while len(password) < n:
        password += random.choice(symbols)
    return password


if __name__ == "__main__":
    n = 8
    print(generate_password(n))

