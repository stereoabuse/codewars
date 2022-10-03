##  Convert A Hex String To RGB
##  5 kyu
##  https://www.codewars.com/kata/5282b48bb70058e4c4000fa7


def hex_string_to_RGB(hex_string):
    return dict(zip('rgb', (int(hex_string[i:i+2],16) for i in range(1, len(hex_string),2))))