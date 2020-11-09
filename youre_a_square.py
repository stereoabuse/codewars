##  You're a square!
##  7 kyu
##  https://www.codewars.com//kata/54c27a33fb7da0db0100040e


def is_square(n):
    if n < 0:
        return False
    return True if (n**0.5)%1 == 0 else False