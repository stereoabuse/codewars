##  Bit Counting
##  6 kyu
##  https://www.codewars.com/kata/526571aae218b8ee490006f4


def countBits(n):
    return sum([int(i) for i in bin(n)[2:]])