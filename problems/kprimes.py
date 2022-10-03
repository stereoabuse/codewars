##  k-Primes
##  5 kyu
##  https://www.codewars.com/kata/5726f813c8dcebf5ed000a6b


import math

def seive(n: int) -> list:
    primes = 2 * [False] + (n-1) * [True]
    for i in range(2, int(n**0.5 + 1.5)):
        for j in range(i*i, n+1, i):
            primes[j] = False
    return [prime for prime, checked in enumerate(primes) if checked]

def primeFactors(n):
    factor_list = []
    while n % 2 == 0:
        factor_list.append(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factor_list.append(i)
            n = n / i
    if n > 2:
        factor_list.append(n)
    return factor_list


def count_Kprimes(k, start, end):
    if start == 0:
        start = 1
    return_list = list()
    for i in range(start, end + 1):
        factors = primeFactors(i)
        if len(factors) == k:
            return_list.append(i)
    return return_list


def puzzle(s):
    return_list = []
    prime_3, prime_7 = set(), set()
    for i in range(1, s):
        primes = primeFactors(i)
        if len(primes) == 3:
            prime_3.add(i)
        elif len(primes) == 7:
            prime_7.add(i)
    prime_1 = set(seive(s))
    for a in prime_1:
        for b in prime_3:
            for c in prime_7:
                if a + c + b == s:
                    return_list.append([a,c,b])
    return len(return_list)
            