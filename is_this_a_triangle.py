##  Is this a triangle?
##  7 kyu
##  https://www.codewars.com//kata/56606694ec01347ce800001b


def is_triangle(a, b, c):
    return sum([a,b,c]) - max([a,b,c]) > max([a,b,c])