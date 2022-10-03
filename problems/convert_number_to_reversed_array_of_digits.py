##  Convert number to reversed array of digits
##  8 kyu
##  https://www.codewars.com/kata/5583090cbe83f4fd8c000051


def digitize(n):
    return [int(c) for c in str(n)[::-1]]