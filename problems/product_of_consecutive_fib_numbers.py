##  Product of consecutive Fib numbers
##  5 kyu
##  https://www.codewars.com//kata/5541f58a944b85ce6d00006a


def fibs(n):
    fib_list = [1,1]
    x, y = 1, 2 
    while y <= n:
        x, y = y, x + y
        fib_list.append(x)
    return fib_list

def productFib(prod):
    if prod == 0:
        return [0, 1, True]
    for index,item in enumerate(fibs(prod)):
        if index < len(fibs(prod))-1:
            if fibs(prod)[index] * fibs(prod)[index+1] == prod:
                return [fibs(prod)[index], fibs(prod)[index+1], True]
        if index < len(fibs(prod))-1:
            if fibs(prod)[index] * fibs(prod)[index+1] < prod < fibs(prod)[index+1] * fibs(prod)[index+2]:
                return [fibs(prod)[index+1], fibs(prod)[index+2], False] 