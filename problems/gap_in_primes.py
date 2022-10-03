##  Gap in Primes
##  5 kyu
##  https://www.codewars.com/kata/561e9c843a2ef5a40c0000a4


def gap(g,m,n):

    if g % 2 != 0:
        return None
    if m % 2 == 0:
        m += 1
    primes = []
    for i in range(m, n, 2):
        for j in range(3, int(i**.5)+1,2):
            if i % j == 0:
                break
        else:
            primes.append(i)
        if len(primes) >= 2 and abs(primes[-1] - primes[-2]) == g:
            return primes[-2:]
        
    return None
    
        
                