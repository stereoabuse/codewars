##  Vowel Count
##  7 kyu
##  https://www.codewars.com//kata/54ff3102c1bad923760001f3


def getCount(inputStr):
    num_vowels = 0
    # your code here
    num_vowels = inputStr.count('a')+inputStr.count('e')+inputStr.count('i')+inputStr.count('o')+inputStr.count('u')
#     num_vowles = num_vowels.count(
    
    return num_vowels