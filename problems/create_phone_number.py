##  Create Phone Number
##  6 kyu
##  https://www.codewars.com//kata/525f50e3b73515a6db000b83


def create_phone_number(n):
    n = [str(i) for i in n]
    part1 = ''.join(n[:3])
    part2 = ''.join(n[3:6])
    part3 = ''.join(n[6:])
    return f'({part1}) {part2}-{part3}'