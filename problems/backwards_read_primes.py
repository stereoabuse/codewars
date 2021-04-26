##  Backwards Read Primes
##  6 kyu
##  https://www.codewars.com/kata/5539fecef69c483c5a000015


import math


def is_prime(x):
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, math.ceil(math.sqrt(x)) + 1, 2):
            if x % i == 0:
                return False
        return True
    

def backwards_prime(start, stop):
    ans = set()
    for i in range(start, stop+1):
        rev_i = int(str(i)[::-1])
        if i in ans:
            continue
        elif is_prime(i) and is_prime(rev_i) and str(i) != str(rev_i):

            ans.add(i)
    return sorted(ans)
