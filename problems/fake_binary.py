##  Fake Binary
##  8 kyu
##  https://www.codewars.com/kata/57eae65a4321032ce000002d


def fake_bin(x):
    num = ''
    for char in x:
        if int(char) < 5:
            num += '0'
        else:
            num += '1'
    return num