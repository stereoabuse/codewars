##  Permutations
##  4 kyu
##  https://www.codewars.com/kata/5254ca2719453dcc0b00027d


from itertools import permutations as perm
def permutations(string):
    return list(set(''.join(i) for i in (perm(string))))