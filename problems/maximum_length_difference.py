##  Maximum Length Difference
##  7 kyu
##  https://www.codewars.com//kata/5663f5305102699bad000056


def mxdiflg(a1, a2):
    a3 = []
    for item in a1:
        for otheritem in a2:
            a3.append(abs(len(item) - len(otheritem)))
    if len(a3) > 0:
        return sorted(a3, reverse = True)[0]
    else:
        return -1