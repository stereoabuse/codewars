##  Find the odd int
##  6 kyu
##  https://www.codewars.com//kata/54da5a58ea159efa38000836


def find_it(seq):
    for item in set(seq):
        if seq.count(item) % 2 != 0:
            return item
