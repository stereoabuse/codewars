##  Scramblies
##  5 kyu
##  https://www.codewars.com/kata/55c04b4cc56a697bb0000048


from collections import Counter
def scramble(s1, s2):
    s1, s2 = Counter(s1), Counter(s2)
    return True if len(s2 - s1) == 0 else False
