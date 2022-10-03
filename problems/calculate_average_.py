##  Calculate average 
##  8 kyu
##  https://www.codewars.com/kata/57a2013acf1fa5bfc4000921


def find_average(array):
    total = sum([i for i in array])
    return total / len(array)