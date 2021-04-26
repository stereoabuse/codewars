##  Playing with digits
##  6 kyu
##  https://www.codewars.com/kata/5552101f47fc5178b1000050


def dig_pow(n,p):
    total = 0
    for d in str(n):
        total += int(d)**p
        p += 1
    if total % n == 0:
        return total // n
    return -1

