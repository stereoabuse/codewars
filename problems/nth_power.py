##  N-th Power
##  8 kyu
##  https://www.codewars.com/kata/57d814e4950d8489720008db


def index(array, n):
    if len(array) > n:
        return array[n] ** n
    return -1