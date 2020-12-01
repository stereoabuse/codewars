##  The Vowel Code
##  6 kyu
##  https://www.codewars.com//kata/53697be005f803751e0015aa


code = [['a', '1'],
['e', '2'],
['i', '3'],
['o', '4'],
['u', '5']]

def encode(st):
    for i in code:
        if i[0] in st:
            st = st.replace(i[0], i[1])
    return st

def decode(st):
    for i in code:
        if i[1] in st:
            st = st.replace(i[1], i[0])
    return st