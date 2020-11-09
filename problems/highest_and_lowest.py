##  Highest and Lowest
##  7 kyu
##  https://www.codewars.com//kata/554b4ac871d6813a03000035


def high_and_low(numbers):
    num_list = [int(i) for i in numbers.split(" ")]
    return f'{sorted(num_list)[-1]} {sorted(num_list)[0]}'