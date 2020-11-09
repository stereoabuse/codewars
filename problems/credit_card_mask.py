##  Credit Card Mask
##  7 kyu
##  https://www.codewars.com//kata/5412509bd436bd33920011bc


def maskify(cc):
    if len(cc) < 4:
        return cc
    return '#' * (len(cc)-4) + cc[-4:]