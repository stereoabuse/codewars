##  Is a number prime?
##  6 kyu
##  https://www.codewars.com//kata/5262119038c0985a5b00029f


import math
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num))+1, 2):
        if num % i == 0:
            return False
    return True