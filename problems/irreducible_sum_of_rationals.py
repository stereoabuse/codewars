##  Irreducible Sum of Rationals
##  6 kyu
##  https://www.codewars.com/kata/5517fcb0236c8826940003c9


from fractions import Fraction, gcd
def sum_fracts(lst):
    total =  str(sum([Fraction(item[0], item[1]) for item in lst])).split("/")
    if len(total) > 1:
        return [int(item) for item in total]
    return None if int(total[0]) == 0 else int(total[0])