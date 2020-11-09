##  Detect Pangram
##  6 kyu
##  https://www.codewars.com//kata/545cedaa9943f7fe7b000048


import string


def is_pangram(s):
    """return true if string contains all letters"""
    letters = [letter.lower() for letter in s if letter.isalpha()]

    return all([i in string.ascii_letters for i in letters]) and len(set(letters)) == 26