##  1RM Calculator
##  6 kyu
##  https://www.codewars.com/kata/595bbea8a930ac0b91000130


def epley(w,r):
    return w * (1 + r / 30)

def mcgothin(w,r):
    return (100 * w) / (101.3 - 2.67123 * r)

def lombardi(w,r):
    return w * r ** 0.10


def calculate_1RM(w,r):
    if r == 1:
        return w
    elif r == 0:
        return 0
    return max(map(round,[epley(w,r), mcgothin(w,r), lombardi(w,r)]))
    