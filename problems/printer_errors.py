##  Printer Errors
##  7 kyu
##  https://www.codewars.com/kata/56541980fa08ab47a0000040


from string import ascii_lowercase

def printer_error(s):
    return f'{sum(1 for c in s if c in ascii_lowercase[13:])}/{len(s)}'