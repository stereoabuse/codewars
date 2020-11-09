##  Basic Math (Add or Subtract)
##  7 kyu
##  https://www.codewars.com//kata/5809b62808ad92e31b000031


def calculate(s):
    return str(sum(int(n) for n in s.replace("minus", "plus-").split("plus")))