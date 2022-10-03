##  Your order, please
##  6 kyu
##  https://www.codewars.com/kata/55c45be3b2079eccff00010f


def order(s):
    sen = [[[x for x in i if x.isdigit()],i] for i in s.split()]
    return ' '.join([i[1] for i in sorted(sen)])