from string import ascii_lowercase, digits
from random import choice, shuffle

def generate_strong_password(length, include_num, include_sc):
    special_chars = "!?=+-()#"
    password = []
    char_pool = ascii_lowercase

    password.append(choice(ascii_lowercase))

    if include_num:
        password.append(choice(digits))
        char_pool += digits

    if include_sc:
        password.append(choice(special_chars))
        char_pool += special_chars

    remaining = length - len(password)
    password.extend(choice(char_pool) for _ in range(remaining))

    shuffle(password)
    return ''.join(password)

for i in range(10):
    print(generate_strong_password(8, True, True))
