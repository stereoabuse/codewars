##  Triple trouble
##  6 kyu
##  https://www.codewars.com/kata/55d5434f269c0c3f1b000058


def triple_double(num1, num2):
    for char in str(num1):
        if char*3 in str(num1) and char*2 in str(num2):
            return 1
    return 0