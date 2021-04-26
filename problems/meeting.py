##  Meeting
##  6 kyu
##  https://www.codewars.com/kata/59df2f8f08c6cec835000012


def meeting(s):
    return ''.join(sorted([f"({', '.join(item.split(':')[::-1])})" for item in s.upper().split(';')]))