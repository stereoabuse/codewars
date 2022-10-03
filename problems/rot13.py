##  Rot13
##  5 kyu
##  https://www.codewars.com/kata/530e15517bc88ac656000716


import codecs

def rot13(message):
    return codecs.encode(message, 'rot_13')
