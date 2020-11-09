##  Sum of Digits / Digital Root
##  6 kyu
##  https://www.codewars.com//kata/541c8630095125aba6000c00


def digital_root(n):
    while True:
        if len(str(sum([int(x) for x in list(str(n))]))) == 1:
            return sum([int(x) for x in list(str(n))])
        n = str(sum([int(x) for x in list(str(n))]))