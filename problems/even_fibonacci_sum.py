##  Even Fibonacci Sum
##  6 kyu
##  https://www.codewars.com/kata/55688b4e725f41d1e9000065


def even_fib(m):
    a,b = 0,1
    evenset = set()
    while b < m:
        if b % 2 == 0:
            evenset.add(b)
        a, b = b, a + b
        
    return sum(evenset)
        