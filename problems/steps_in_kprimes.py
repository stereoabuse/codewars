##  Steps in k-primes
##  6 kyu
##  https://www.codewars.com/kata/5a48948e145c46820b00002f


import math


def seive(n: int) -> list:
    primes = 2 * [False] + (n - 1) * [True]
    for i in range(2, int(n ** 0.5 + 1.5)):
        for j in range(i * i, n + 1, i):
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


def count_kprimes(k, start, end):
    if start == 0:
        start = 1
    return_list = list()
    for i in range(start, end + 1):
        factors = primeFactors(i)
        if len(factors) == k:
            return_list.append(i)
    return return_list


def kprimes_step(k, step, start, end):
    kstepprimes = []
    all_k = set([i for i in count_kprimes(k, start, end)])
#     for i in range(len(all_k)-1):
#             if (all_k[i + 1]) - all_k[i] == step:
#                 kstepprimes.append([all_k[i], all_k[i + 1]])
    for item in all_k:
        
        for otheritem in all_k:
            to_add = []
            if abs(item - otheritem) == step and sorted([item, otheritem]) not in kstepprimes:
                kstepprimes.append(sorted([item, otheritem]))

    return sorted(kstepprimes)