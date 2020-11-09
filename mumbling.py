##  Mumbling
##  7 kyu
##  https://www.codewars.com//kata/5667e8f4e3f572a8f2000039


def accum(s):
    result = ''
    for number, letter in enumerate(s):
        add = (letter.upper() + number * letter.lower())
        result += add
        if number < len(s)-1:
            result += '-'
    return result