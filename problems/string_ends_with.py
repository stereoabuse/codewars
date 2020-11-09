##  String ends with?
##  7 kyu
##  https://www.codewars.com//kata/51f2d1cafc9c0f745c00037d


def solution(string, ending):
    return True if ending == '' else string[-(len(ending)):] == ending
    