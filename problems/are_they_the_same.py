##  Are they the "same"?
##  6 kyu
##  https://www.codewars.com/kata/550498447451fbbd7600041c


def comp(array1, array2):
    try:
        return sorted([i**2 for i in array1]) == sorted(array2)
    except:
        TypeError
        return False
