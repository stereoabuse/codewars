##  Breaking chocolate problem
##  7 kyu
##  https://www.codewars.com//kata/534ea96ebb17181947000ada


def breakChocolate(n, m):
    if n * m > 1:
        return (n * m) -1 
    else:
        return 0