##  Character with longest consecutive repetition
##  6 kyu
##  https://www.codewars.com//kata/586d6cefbcc21eed7a001155


from itertools import groupby
def longest_repetition(chars):
    if not chars:
        return ('', 0)
    groups = groupby(chars)
    result = [(c, sum(1 for _ in l)) for c, l in groups ]
    return sorted(result, key=lambda x: x[1], reverse=True)[0]
longest_repetition('aaabb')