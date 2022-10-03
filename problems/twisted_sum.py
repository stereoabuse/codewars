##  Twisted Sum
##  6 kyu
##  https://www.codewars.com/kata/527e4141bb2ea5ea4f00072f


def digit_sum(x):
    return sum(int(i) for i in str(x))

def compute_sum(n):
    return sum(digit_sum(i) for i in range(n+1))