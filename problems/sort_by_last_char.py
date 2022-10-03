##  Sort by Last Char
##  7 kyu
##  https://www.codewars.com/kata/57eba158e8ca2c8aba0002a0


def last(s):
    return sorted(s.split(), key= lambda x:x[-1])