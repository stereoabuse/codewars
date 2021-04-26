##  IQ Test
##  6 kyu
##  https://www.codewars.com/kata/552c028c030765286c00007d


def iq_test(numbers):
    evens = [int(n) for n in numbers.split(" ") if int(n) % 2 == 0]
    odds = [int(n) for n in numbers.split(" ") if int(n) % 2 != 0]
    if len(evens) == 1:
        return numbers.split(" ").index(str(evens[0]))+ 1
    return numbers.split(" ").index(str(odds[0])) + 1