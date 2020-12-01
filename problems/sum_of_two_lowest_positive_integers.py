##  Sum of two lowest positive integers
##  7 kyu
##  https://www.codewars.com//kata/558fc85d8fd1938afb000014


def sum_two_smallest_numbers(numbers):
    return sorted(numbers)[0] + sorted(numbers)[1]