##  Binary Addition
##  7 kyu
##  https://www.codewars.com/kata/551f37452ff852b7bd000139


def add_binary(a,b):
    return str(bin(a+b)).replace('0b','')