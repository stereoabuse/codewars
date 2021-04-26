##  Sum Mixed Array
##  8 kyu
##  https://www.codewars.com/kata/57eaeb9578748ff92a000009


def sum_mix(arr):
    return sum([x if int(x) == x else int(x) for x in arr])