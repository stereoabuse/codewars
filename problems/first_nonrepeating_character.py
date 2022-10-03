##  First non-repeating character
##  5 kyu
##  https://www.codewars.com/kata/52bc74d4ac05d0945d00054e


def first_non_repeating_letter(string):
    ans = ''
    for char in string:
        if string.lower().count(char.lower()) == 1:
            ans = char
            break
    return ans if ans else ''