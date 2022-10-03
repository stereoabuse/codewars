##  Counting Duplicates
##  6 kyu
##  https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1


def duplicate_count(text):
    text = text.lower()
    d = dict()
    for char in text:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    return len([i for i in d if d[i] > 1])
     