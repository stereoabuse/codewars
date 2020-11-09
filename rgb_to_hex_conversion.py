##  RGB To Hex Conversion
##  5 kyu
##  https://www.codewars.com//kata/513e08acc600c94f01000001


def rgb(r, g, b):
    rgb_list = [r, g, b]
    hexvalue = ""
    for color in rgb_list:
        if color >= 255:
            hexvalue += "FF"
        elif color <= 0:
            hexvalue += "00"
        elif len(hex(color)) == 3:
            hexvalue += f"0{hex(color)[2]}"
        else:
            hexvalue += hex(color)[2:]
    return hexvalue.upper()