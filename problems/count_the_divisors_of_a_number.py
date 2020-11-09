##  Count the divisors of a number
##  7 kyu
##  https://www.codewars.com//kata/542c0f198e077084c0000c2e


def divisors(n):
    return len([i for i in range(1, (n // 2) + 1) if n % i == 0]) + 1