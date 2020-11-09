##  uniq (UNIX style)
##  6 kyu
##  https://www.codewars.com//kata/52249faee9abb9cefa0001ee


import itertools

def uniq(seq):
#     ans = []
    return [list(g)[0] for k, g in itertools.groupby(seq)]

