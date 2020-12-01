##  Sum of odd numbers
##  7 kyu
##  https://www.codewars.com//kata/55fd2d567d94ac3bc9000064


def row_sum_odd_numbers(n):
    total = 0
    row_sum= 0
    for i in range(n-1,0, -1):
        total += i
    starting_odd = total * 2 + 1
    for i in range(1,n+1):
        row_sum += starting_odd
        starting_odd += 2
    return row_sum