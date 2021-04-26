##  FIXME: Replace all dots
##  8 kyu
##  https://www.codewars.com/kata/596c6eb85b0f515834000049


import re
def replace_dots(str):
    return re.sub(r"\.", "-", str)