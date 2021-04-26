##  Exes and Ohs
##  7 kyu
##  https://www.codewars.com/kata/55908aad6620c066bc00002a


def xo(s):
    if s.lower().count('x') == s.lower().count('o'):
        return True
    else:
        return False