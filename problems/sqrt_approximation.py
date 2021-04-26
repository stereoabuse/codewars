##  Sqrt approximation
##  6 kyu
##  https://www.codewars.com/kata/52ecde1244751a799b00018a


def sqrt_approximation(number):
    for i in range(1,number):
        if i * i == number:
            return i
        if i * i > number:
            return [i-1, i]