##  Convert a string to an array
##  8 kyu
##  https://www.codewars.com/kata/57e76bc428d6fbc2d500036d


def string_to_array(s):
    if not s:
        return ['']
    return s.split()