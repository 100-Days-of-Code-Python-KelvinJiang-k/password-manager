import random

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

NUM_LETTERS = 4
NUM_SYMBOLS = 2
NUM_NUMBERS = 2


class PasswordGenerator:

    def __init__(self):
        pass

    def generate(self):
        password_letters = [random.choice(LETTERS) for i in range(NUM_LETTERS)]
        password_symbols = [random.choice(SYMBOLS) for i in range(NUM_SYMBOLS)]
        password_numbers = [random.choice(NUMBERS) for i in range(NUM_NUMBERS)]
        password_format = password_letters + password_symbols + password_numbers

        random.shuffle(password_format)
        password = ''.join(password_format)
        return password
