##  Find the unique number
##  6 kyu
##  https://www.codewars.com//kata/585d7d5adb20cf33cb000235


def find_uniq(arr):
    if sorted(arr)[0] == sorted(arr)[1]:
        return sorted(arr)[-1]
    return sorted(arr)[0]