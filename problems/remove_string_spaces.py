##  Remove String Spaces
##  8 kyu
##  https://www.codewars.com/kata/57eae20f5500ad98e50002c5


def no_space(x):
    return "".join([a for a in x.split(' ')])