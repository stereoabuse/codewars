##  Where my anagrams at?
##  5 kyu
##  https://www.codewars.com//kata/523a86aa4230ebb5420001e1


from collections import Counter
def anagrams(word, words):
    return [i for i in words if Counter(i) == Counter(word)]
