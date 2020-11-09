##  First non-repeating character
##  5 kyu
##  https://www.codewars.com//kata/52bc74d4ac05d0945d00054e


from collections import Counter

def first_non_repeating_letter(string):
    s = Counter(string.lower())
    for c in string:
        if s[c.lower()] == 1:
            return c
    return ""