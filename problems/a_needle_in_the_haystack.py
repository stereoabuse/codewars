##  A Needle in the Haystack
##  8 kyu
##  https://www.codewars.com/kata/56676e8fabd2d1ff3000000c


def find_needle(haystack):
    for index, item in enumerate(haystack):
        if item == 'needle':
            return f'found the needle at position {index}'
