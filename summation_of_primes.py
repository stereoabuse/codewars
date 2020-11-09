##  Summation Of Primes
##  6 kyu
##  https://www.codewars.com//kata/59ab0ca4243eae9fec000088


def summationOfPrimes(primes):
  numbers = set(range(primes, 1, -1))
  primelist = []
  while numbers:
      p = numbers.pop()
      primelist.append(p)
      numbers.difference_update(set(range(p*2, primes+1,p)))
  return sum(primelist)
  