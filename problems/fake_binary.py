##  Fake Binary
##  8 kyu
##  https://www.codewars.com/kata/57eae65a4321032ce000002d


def fake_bin(x):
#     return ''.join(['0'  if int(char) < 5 for char in x else '1'])
    num = ''
    for char in x:
        if int(char) < 5:
            num += '0'
        else:
            num += '1'
    return num