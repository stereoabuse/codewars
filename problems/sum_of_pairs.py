##  Sum of pairs
##  5 kyu
##  https://www.codewars.com//kata/54d81488b981293527000c8f


def sum_pairs(ints, s):
    table = set()    
    for b in ints:
        a = s - b       
        if a in table:
            return [a, b]       
        table.add(b)
    return None