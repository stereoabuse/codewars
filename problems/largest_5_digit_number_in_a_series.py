##  Largest 5 digit number in a series
##  7 kyu
##  https://www.codewars.com/kata/51675d17e0c1bed195000001


def solution(digits):
    biggest = 0
    for index in range(len(digits) - 4):
        if int(digits[index:index+5]) > biggest:
            biggest = int(digits[index:index+5]) 
    return biggest