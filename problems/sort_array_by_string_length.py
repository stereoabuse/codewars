##  Sort array by string length
##  7 kyu
##  https://www.codewars.com/kata/57ea5b0b75ae11d1e800006c


def sort_by_length(arr):
    return sorted(arr, key=len)