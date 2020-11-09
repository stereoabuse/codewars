##  Pandemia 🌡️
##  7 kyu
##  https://www.codewars.com//kata/5e2596a9ad937f002e510435


def infected(s):
    if not "1" in s:
        return 0
    infected = 0
#     pop = len(s.replace('X',''))
    conts = [i for i in s.split('X')]
    for cont in conts:
        if '1' in cont:
            infected += len(cont)
        
    return infected/(len(s.replace('X',''))) * 100