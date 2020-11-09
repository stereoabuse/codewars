##  Integers: Recreation One
##  5 kyu
##  https://www.codewars.com//kata/55aa075506463dac6600010d


import math
from functools import reduce


def factors(n):
    factor_set = ([i, n // i] for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0)
    return set(reduce(list.__add__, factor_set))


def list_squared(m, n):
    return_list = []
    for i in range(m, n + 1):
        divs_of_i = factors(i)
        square_list = [num ** 2 for num in divs_of_i]
        if math.sqrt(sum(square_list)) == int(math.sqrt(sum(square_list))):
            return_list.append([i, sum(square_list)])

    return return_list