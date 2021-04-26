##  Difference Of Squares
##  7 kyu
##  https://www.codewars.com/kata/558f9f51e85b46e9fa000025


def difference_of_squares(n):
    sum_of_squares = 0
    sums = 0
    for i in range(n+1):
        sum_of_squares += i**2
        
    for j in range(n+1):
        sums += j
    square_of_sums = sums ** 2
    return abs(sum_of_squares- square_of_sums)