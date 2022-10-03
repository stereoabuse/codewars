##  Abbreviate a Two Word Name
##  8 kyu
##  https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3


def abbrevName(name):
    name = name.split(' ')
    return f'{name[0][0].upper()}.{name[1][0].upper()}'