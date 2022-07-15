from helpers import *
import sys

if __name__ == '__main__':

    try:
        str_to_find = sys.argv[1]  # to get input from cmd line (eg. python main.py jim)
        find_word_in_files(str_to_find=str_to_find)
    except IndexError:
        print("Please provide an argument in the execution!\n"
              "Example: python main.py jim")
