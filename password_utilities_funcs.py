"""
The following python program will generate random number, ascii (lower or upper) and
puncuations based on your selection.

Notes:
    - Should add security check to see if password is a valid password. 
    - To add on, from a security perspective, we should not allow "\0"
"""

import string
import re
from random import choice, choices, randint, sample

DIGITS = string.digits
ASCII_UPPER = string.ascii_uppercase
ASCII_LOWER = string.ascii_lowercase
PUNCTUATIONS = string.punctuation


class random_gen:
    """Generates a random password based on security level and string len and base (ASCII or numeric)."""

    def __init__(self, string_len, base):
        """
        The following will generate a string base on the functions that you specify.
        """
        self.string_len = int(string_len)
        self.base = base

    def create_rand_pass_sec_level_one(self):
        """
        The following function will generate a random password based on the security level 1 requirements
            - Special character 1
            - ASCII Upper 1
        """
        rand_punc = choice(PUNCTUATIONS)
        rand_upper = choice(ASCII_UPPER)
        remain_char = self.string_len - 3
        if self.base == 'ascii':
            rand_num = randint(0, 9)
            rand_strs = ''.join(choice(ASCII_LOWER)
                                for i in range(remain_char))
            password_chars_selection = str(
                rand_num) + rand_punc + rand_strs + rand_upper
            return ''.join(sample(password_chars_selection, self.string_len))
        elif self.base == 'numeric':
            rand_lower = choice(ASCII_LOWER)
            rand_strs = ''.join(choice(DIGITS) for i in range(remain_char))
            password_chars_selection = rand_lower + rand_punc + rand_strs + rand_upper
            return ''.join(sample(password_chars_selection, self.string_len))

    def create_rand_pass_sec_level_two(self):
        """
        The following function will generate a random password based on the security level 2 requirements
            - Special character 2
            - ASCII Upper 2
        """
        rand_punc = ''.join(choices(PUNCTUATIONS, k=2))
        rand_upper = ''.join(choices(ASCII_UPPER, k=2))
        remain_char = self.string_len - 4
        if self.base == 'ascii':
            rand_num = choices(DIGITS, k=2)
            rand_strs = ''.join(choice(ASCII_LOWER)
                                for i in range(remain_char))
            password_chars_selection = str(
                rand_num) + rand_punc + rand_strs + rand_upper
            return ''.join(sample(password_chars_selection, self.string_len))
        elif self.base == 'numeric':
            rand_lower = choices(ASCII_LOWER, k=2)
            rand_strs = ''.join(choice(DIGITS) for i in range(remain_char))
            password_chars_selection = rand_lower + rand_punc + rand_strs + rand_upper
            return ''.join(sample(password_chars_selection, self.string_len))


class custom_pass_checker(object):
    """
    Creates a custom password based on your specifications
    """

    def __init__(self, given_password):
        self.given_password = given_password
        

    def password_checker(self):
        """Password algorithm to check whether the password is secure or not."""
        pass_to_check = self.given_password
        bool_num_present = bool(re.search(r'\d', pass_to_check))
        bool_ascii_upper_present = bool(re.search(r'[A-Z]', pass_to_check))
        bool_ascii_lower_present = bool(re.search(r'[a-z]', pass_to_check))
        bool_punc_present = False
        for string in pass_to_check:
            if string in PUNCTUATIONS:
                bool_punc_present = True
        if len(pass_to_check) >= 12 and bool_ascii_lower_present and bool_ascii_upper_present and bool_num_present and bool_punc_present:
            return "Password Security level is High."
        elif 8 <= len(pass_to_check) < 12 and bool_ascii_lower_present and bool_ascii_upper_present and bool_num_present and bool_punc_present:
            return "Password Security level is Medium."
        else:
            return "Password Secuurity level is Low."


# def test():
#     r = random_gen('8', 'ascii')
#     a = custom_pass_checker(r.create_rand_pass_sec_level_one())
#     # print(r.create_rand_pass_sec_level_one())
#     # print(r.create_rand_pass_sec_level_two())
#     print(a.password_checker())

# test()
