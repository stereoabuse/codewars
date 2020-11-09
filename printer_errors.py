##  Printer Errors
##  7 kyu
##  https://www.codewars.com//kata/56541980fa08ab47a0000040


def printer_error(s):
    err = 0
    for i in s:
        if i in 'nopqrstuvwxyz':
            err += 1
    return "{}/{}".format(err, len(s))