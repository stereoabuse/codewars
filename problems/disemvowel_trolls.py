##  Disemvowel Trolls
##  7 kyu
##  https://www.codewars.com/kata/52fba66badcd10859f00097e


def disemvowel(string):
    return string.translate({ord(i): None for i in 'aeiouAEIOU'})