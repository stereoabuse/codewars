##  Find the odd int
##  6 kyu
##  https://www.codewars.com/kata/54da5a58ea159efa38000836


from itertools import groupby

def find_it(seq):
    return [i for i in [list(g) for k,g in groupby(sorted(seq))] if len(i)%2 != 0][0][0]
