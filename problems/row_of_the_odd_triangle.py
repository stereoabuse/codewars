##  Row of the odd triangle
##  6 kyu
##  https://www.codewars.com/kata/5d5a7525207a674b71aa25b5


def odd_row(n):
    total = 0
    returnlist = []
    for i in range(n-1,0, -1):
        total += i
    starting_odd = total * 2 + 1
    for i in range(1,n+1):
        returnlist.append(starting_odd)
        starting_odd += 2
    return returnlist