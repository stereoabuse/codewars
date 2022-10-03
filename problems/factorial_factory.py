##  Factorial Factory
##  7 kyu
##  https://www.codewars.com/kata/528e95af53dcdb40b5000171


# This function should return n!
def factorial(n):
    if n == 0 or n == 1:
        return 1
    if n < 0:
        return None
    return n * factorial(n-1)