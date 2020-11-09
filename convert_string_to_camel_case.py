##  Convert string to camel case
##  6 kyu
##  https://www.codewars.com//kata/517abf86da9663f1d2000003


import re
def to_camel_case(text):
    if text == '':
        return text
    textlist = re.split('-|_', text)
    if textlist[0][0].isupper():
        return ''.join(i.capitalize() for i in textlist)
    return textlist[0]+''.join(i.capitalize() for i in textlist[1:])