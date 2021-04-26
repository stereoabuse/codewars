##  Does my number look big in this?
##  6 kyu
##  https://www.codewars.com/kata/5287e858c6b5a9678200083c


def narcissistic(value):
    total = 0
    for digit in str(value):
        total += int(digit) ** len(str(value))
    return value == total