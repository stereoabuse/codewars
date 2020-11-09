##  Mean Square Error
##  5 kyu
##  https://www.codewars.com//kata/51edd51599a189fe7f000015


def solution(a, b):

    return sum([abs(a[i] - b[i]) ** 2 for i in range(len(a))]) / len(a)