##  Find the Mine!
##  6 kyu
##  https://www.codewars.com//kata/528d9adf0e03778b9e00067e


def mineLocation(field):
    for i in range(len(field)):
        for j in range(len(field)):
            if '1' in str(field[i][j]):
                return [i, j]