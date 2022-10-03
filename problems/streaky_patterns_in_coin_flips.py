##  Streaky Patterns in Coin Flips
##  7 kyu
##  https://www.codewars.com/kata/5c1ac4f002c59c725900003f


from itertools import groupby


def check_sequence(sequence, l, n):
    chunks = [''.join(list(g)) for k, g in groupby(sequence)]
    return n == sum(1 for chunk in chunks if len(chunk) == l)
