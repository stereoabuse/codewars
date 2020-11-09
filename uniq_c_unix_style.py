##  uniq -c (UNIX style)
##  5 kyu
##  https://www.codewars.com//kata/52250aca906b0c28f80003a1


from itertools import groupby
def uniq_c(seq):
    return [(a, len(list(b))) for a, b in groupby(seq)]