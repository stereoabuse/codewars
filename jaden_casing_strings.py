##  Jaden Casing Strings
##  7 kyu
##  https://www.codewars.com//kata/5390bac347d09b7da40006f6


def toJadenCase(string):
    words = string.split(' ')
    newstring = ''
    for word in words:
        word = word.capitalize()
        newstring += word + ' '
    return newstring.rstrip()
