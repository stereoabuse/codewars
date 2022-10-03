##  Exclamation marks series #11: Replace all vowel to exclamation mark in the sentence
##  8 kyu
##  https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed


def replace_exclamation(s):
    word = ''
    for letter in s:
        if letter in 'aeiouAEIOU':
            word += '!'
        else:
            word += letter
    return word