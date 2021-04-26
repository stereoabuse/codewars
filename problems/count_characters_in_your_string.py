##  Count characters in your string
##  6 kyu
##  https://www.codewars.com/kata/52efefcbcdf57161d4000091


def count(string):
    list1 = {}
    for item in string:
        if item not in list1:
            list1[item] = 0
        list1[item] += 1
    return list1