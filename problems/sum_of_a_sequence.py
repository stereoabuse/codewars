##  Sum of a sequence
##  7 kyu
##  https://www.codewars.com//kata/586f6741c66d18c22800010a


def sequence_sum(begin, end, step):
    return sum([i for i in range(begin, end+1, step)])