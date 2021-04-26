##  Memoized Fibonacci
##  5 kyu
##  https://www.codewars.com/kata/529adbf7533b761c560004e5


import functools

@functools.lru_cache(maxsize=None)
def fibonacci(n):
    if n in [0, 1]:
        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)