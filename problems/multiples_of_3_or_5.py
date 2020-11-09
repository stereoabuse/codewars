##  Multiples of 3 or 5
##  6 kyu
##  https://www.codewars.com//kata/514b92a657cdc65150000006


def solution(n):
    mult_sum = 0
    for i in range (3, n):
        if i % 3 == 0 or i % 5 ==0:
            mult_sum += i
    return mult_sum