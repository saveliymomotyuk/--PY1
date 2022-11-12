
from string import ascii_letters, digits
from random import sample

def get_random_password(length: int = 8) -> str:
    str_ = ''.join(sample(ascii_letters + digits, length))

    return str_



print(get_random_password())
