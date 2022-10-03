##  IQ Test
##  Retired
##  https://www.codewars.com/kata/552c028c030765286c00007d


def iq_test(numbers):
    numbers = [int(i) for i in numbers.split(' ')]
    assignments =  ['even' if i % 2 == 0 else 'odd' for i in numbers]
    if assignments.count('even') == 1:
        return assignments.index('even')+1
    else:
        return assignments.index('odd')+1