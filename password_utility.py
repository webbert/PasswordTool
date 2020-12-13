"""
The following Utility is a password tool.
This allows the user to create a password and check whether the password is secure based on High, Medium and Low.
The tool also allows you to store passwords based on your pin you specify.
"""
import password_utilities_funcs
import 
import argparse

INDEX_ONE = 0
INDEX_TWO = 1
INDEX_THREE = 2


def pass_db(file_name):
    pass


def pass_checker(p_word):
    """
    The following function will check the password and determine its security level.
    """
    password_level = password_utilities_funcs.custom_pass_checker(p_word)
    return(password_level.password_checker())


def pass_creation(arg_list):
    """
    The following function will create a password based on the specifications given by the user.
    """
    create_pass = password_utilities_funcs.random_gen(
        arg_list[INDEX_ONE], arg_list[INDEX_THREE])
    if arg_list[INDEX_TWO] == 1:
        return create_pass.create_rand_pass_sec_level_one()
    elif arg_list[INDEX_TWO] == 2:
        return create_pass.create_rand_pass_sec_level_two()
    else:
        print("Error code 2")
        exit()


def function_filter(arg):
    no_chars = arg.no_char
    s_level = arg.level
    p_base = arg.base
    p_word = arg.pword

    if p_word is not None:
        print(pass_checker(p_word))
    elif(no_chars and s_level and p_base) != None:
        arg_list = [no_chars, s_level, p_base]
        print(pass_creation(arg_list))
    else:
        print("Error code 1")
        exit()


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Password utility tool done by webbert")
    pass_create = parser.add_argument_group(
        'Password Creation utiliy', description="The following group will allow the user to create a password. ")
    pass_check = parser.add_argument_group(
        'Password Security Check utility', description="The following group will allow the user to check the security of the password.")
    pass_create.add_argument('-c', '--char', dest='no_char', type=int,
                             metavar="", help='Number of Characters (recommended no of chars: 12 or more)')
    pass_create.add_argument('-s', '--level', dest='level', type=int,
                             choices=[1, 2], metavar="", help='Security level of the password (recommended security level: 2)')
    pass_create.add_argument('-b', '--base', dest='base', type=str, choices=[
        'ascii', 'numeric'], metavar="", help='Base defines which characters will be used the most (recommended base : ascii)')
    pass_check.add_argument('-p', dest='pword', type=str, metavar="",
                            help='This option allows the user to check whether the password is secure.')
    arg = parser.parse_args()
    return arg


def tests():
    pass


def main():
    arg = parse_arguments()
    function_filter(arg)


if __name__ == "__main__":
    main()
