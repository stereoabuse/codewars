##  Remove duplicate words
##  7 kyu
##  https://www.codewars.com/kata/5b39e3772ae7545f650000fc


def remove_duplicate_words(s):
    s = s.split()
    unique_words = []
    for word in s:
        if word not in unique_words:
            unique_words.append(word)
    return ' '.join(unique_words)