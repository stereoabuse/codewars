##  Summing a number's digits
##  7 kyu
##  https://www.codewars.com/kata/52f3149496de55aded000410


def sum_digits(number):
    return sum(int(x) for x in str(abs(number)))