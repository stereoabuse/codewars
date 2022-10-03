##  Sum without highest and lowest number
##  8 kyu
##  https://www.codewars.com/kata/576b93db1129fcf2200001e6


def sum_array(arr):
    if arr and len(arr) > 2:
        return sum(arr) - max(arr) - min(arr)
    return 0