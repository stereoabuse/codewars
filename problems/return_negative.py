##  Return Negative
##  8 kyu
##  https://www.codewars.com/kata/55685cd7ad70877c23000102


def make_negative( number ):
    # ...
    if number == 0:
        return 0
    elif number < 0:
        return number
    else:
        return -number