##  Find the first non-consecutive number
##  8 kyu
##  https://www.codewars.com/kata/58f8a3a27a5c28d92e000144


def first_non_consecutive(arr):
    for index, val in enumerate(arr):
        if index > 0:
            if val - arr[index-1] != 1:
                return val
    return None