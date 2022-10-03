##  RGB To Hex Conversion
##  5 kyu
##  https://www.codewars.com/kata/513e08acc600c94f01000001


def rgb(r,g,b):
    ans = ''
    for color in [r,g,b]:
        if int(color) > 255:
            ans += 'FF'
        elif int(color) < 0:
            ans += '00'
        else:
            ans += hex(color)[2:].rjust(2,'0')
    return ans.upper()