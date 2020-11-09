##  Number Zoo Patrol
##  6 kyu
##  https://www.codewars.com//kata/5276c18121e20900c0000235


def find_missing_number(numbers):
    numbers = set(numbers)
    if len(numbers) == 0:
        return 1
    for i in range(1,max(numbers)+2):
        if i not in numbers:
            return i