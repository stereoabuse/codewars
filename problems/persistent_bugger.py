##  Persistent Bugger.
##  6 kyu
##  https://www.codewars.com//kata/55bf01e5a717a0d57e0000ec


def persistence(n):
    """takes in a positive n and returns the multiplicative persistence"""
    count = 0
    if len(str(n)) == 0:
        return 0
    while len(str(n))> 1:
        p = 1
        for i in str(n):
            p *= int(i)
        n, count = p, count + 1
    return count
    