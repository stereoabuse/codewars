##  All Star Code Challenge #20
##  7 kyu
##  https://www.codewars.com/kata/5865a75da5f19147370000c7


def add_arrays(a,b): 
    if len(a) == len(b):
        return [a[i] + b[i] for i in range(len(a))]
    raise Error