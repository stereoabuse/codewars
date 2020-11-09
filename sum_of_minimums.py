##  Sum of Minimums!
##  7 kyu
##  https://www.codewars.com//kata/5d5ee4c35162d9001af7d699


def sum_of_minimums(numbers):
    return sum([min(row) for row in numbers])