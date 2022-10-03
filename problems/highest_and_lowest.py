##  Highest and Lowest
##  7 kyu
##  https://www.codewars.com/kata/554b4ac871d6813a03000035


def high_and_low(numbers):
    big = max(int(i) for i in numbers.split(' '))
    small = min(int(i) for i in numbers.split(' '))
    return f'{big} {small}'