##  Descending Order
##  7 kyu
##  https://www.codewars.com/kata/5467e4d82edf8bbf40000155


def Descending_Order(num):
    numlist = sorted(list(str(num)), reverse = True)
    newint = ""
    for item in numlist:
        newint += item
    return int(newint)