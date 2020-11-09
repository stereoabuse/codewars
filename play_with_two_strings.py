##  Play with two Strings
##  5 kyu
##  https://www.codewars.com//kata/56c30ad8585d9ab99b000c54


def work_on_strings(a,b):
    a_answer = ''
    b_answer = ''
    for x in b:
        if (a.casefold().count(x.casefold()) == 0) or (a.casefold().count(x.casefold()) % 2 == 0):
            b_answer += x
        elif a.casefold().count(x.casefold()) % 2 == 1:
            b_answer += x.swapcase()
    for y in a:
        if (b.casefold().count(y.casefold()) == 0) or (b.casefold().count(y.casefold()) % 2 == 0):
            a_answer += y
        elif b.casefold().count(y.casefold()) % 2 == 1:
            a_answer += y.swapcase()
    return a_answer + b_answer