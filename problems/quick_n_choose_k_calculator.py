##  Quick (n choose k) calculator
##  6 kyu
##  https://www.codewars.com/kata/55b22ef242ad87345c0000b2


from scipy.special import comb

def choose(n,k):
    return comb(n,k, exact=True)