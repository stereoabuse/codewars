##  Remove First and Last Character
##  8 kyu
##  https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0


def remove_char(s):
    return '' if len(s) == s else s[1:-1]