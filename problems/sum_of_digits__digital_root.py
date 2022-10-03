##  Sum of Digits / Digital Root
##  6 kyu
##  https://www.codewars.com/kata/541c8630095125aba6000c00


def digit_sum(x):
    return sum(int(i) for i in str(x))

def digital_root(n):
    return n if len(str(n)) == 1 else digital_root(digit_sum(n))
