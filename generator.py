'''Script used to generate the password'''

import random

UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_LETTERS = "abcdefghijklmnopqrstuvwxyz"
NUMBERS = "0123456789"
SPECIAL_CHARACTERS = " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

def create_password(length: int, checks, chars: str):
    '''
    Uses time for creating pseudo random strings that can be used
    for passowords
    '''
    # Defining the characters that will be used for creating password
    chars_to_use = ""
    if checks[0]:
        chars_to_use += LOWER_LETTERS
    if checks[1]:
        chars_to_use += UPPER_LETTERS
    if checks[2]:
        chars_to_use += NUMBERS
    if chars != "":
        chars_to_use += chars

    # Making a password
    password = ""
    for i in range(length):
        password += chars_to_use[random.randrange(0, len(chars_to_use))]

    print(password)
    return password
