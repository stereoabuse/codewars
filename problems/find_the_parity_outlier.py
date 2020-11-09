##  Find The Parity Outlier
##  6 kyu
##  https://www.codewars.com//kata/5526fc09a1bbd946250002dc


def find_outlier(integers):
    evens = [item for item in integers[:3] if item %2 ==0]
    odds = [item for item in integers[:3] if item %2 !=0]

    if len(odds) > len(evens):
        for item in integers:
            if item % 2 == 0:
                return item
    for item in integers:
        if item % 2 != 0:
            return item
        