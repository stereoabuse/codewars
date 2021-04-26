##  STRONGN Strong Number (Special Numbers Series #2) 
##  7 kyu
##  https://www.codewars.com/kata/5a4d303f880385399b000001


from math import factorial
def strong_num(number):
    return "STRONG!!!!" if number == sum([factorial(int(d)) for d in str(number)]) else "Not Strong !!"