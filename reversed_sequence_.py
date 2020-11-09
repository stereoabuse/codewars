##  Reversed sequence 
##  8 kyu
##  https://www.codewars.com//kata/5a00e05cc374cb34d100000d


def reverse_seq(n):
    return sorted([n for n in range(1,n+1)], reverse=True)