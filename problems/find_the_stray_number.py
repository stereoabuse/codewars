##  Find the stray number
##  7 kyu
##  https://www.codewars.com//kata/57f609022f4d534f05000024


from collections import Counter

def stray(arr):
    return Counter(arr).most_common()[-1][0]