##  Break camelCase
##  6 kyu
##  https://www.codewars.com//kata/5208f99aee097e6552000148


import re

def solution(text):
    answer = re.findall('[A-Z]*[a-z]+', text)
    return ' '.join(answer)