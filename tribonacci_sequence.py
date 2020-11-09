##  Tribonacci Sequence
##  6 kyu
##  https://www.codewars.com//kata/556deca17c58da83c00002db


def tribonacci(signature, n):
    a, b, c = signature[0], signature[1], signature[2]
    while len(signature) < n:
        a,b,c = b, c, a+b+c
        signature.append(c)
    return signature[:n]
    

    
    