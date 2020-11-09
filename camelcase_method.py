##  CamelCase Method
##  6 kyu
##  https://www.codewars.com//kata/587731fda577b3d1b0001196


def camel_case(string):
    return ''.join([word.title() for word in string.split()])