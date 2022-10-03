##  Simple Fun #2: Circle of Numbers
##  7 kyu
##  https://www.codewars.com/kata/58841cb52a077503c4000015


def circle_of_numbers(n, fst):
    return list(range(n))[(n//2 + fst)%n]