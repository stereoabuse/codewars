##  Longest Common Subsequence
##  5 kyu
##  https://www.codewars.com/kata/52756e5ad454534f220001ef


from itertools import combinations

def lcs(x,y):
    option_x = set()
    option_y = set()
    for i in range(1, len(x)+1):
        for item in combinations(x,i):
            option_x.add(''.join(item))
    for i in range(1, len(y)+1):
        for item in combinations(y, i):
            option_y.add(''.join(item))
    try:
        return max((item for item in option_x if item in option_y), key=len)
    except ValueError:
        return ''
