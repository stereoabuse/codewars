##  Shortest Word
##  7 kyu
##  https://www.codewars.com//kata/57cebe1dc6fdc20c57000ac9


def find_short(s):
    # your code here
    return sorted([len(word) for word in s.split()])[0]