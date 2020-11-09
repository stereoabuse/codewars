##  Count the smiley faces!
##  6 kyu
##  https://www.codewars.com//kata/583203e6eb35d7980400002a


import re

def count_smileys(arr):
    return sum([bool(re.match(r'[;:][-~]?[)D]', s)) for s in arr])