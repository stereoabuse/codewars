##  Ones and Zeros
##  7 kyu
##  https://www.codewars.com//kata/578553c3a1b8d5c40300037c


def binary_array_to_number(arr):
    return sum([(2**i) for i in range(len(arr)) if arr[::-1][i] == 1])