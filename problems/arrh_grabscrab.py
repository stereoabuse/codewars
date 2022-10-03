##  Arrh, grabscrab!
##  6 kyu
##  https://www.codewars.com/kata/52b305bec65ea40fe90007a7


from collections import Counter
def grabscrab(word, possible_words):
    return [i for i in possible_words if Counter(word) == Counter(i)]