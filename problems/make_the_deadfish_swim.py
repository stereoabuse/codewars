##  Make the Deadfish Swim
##  6 kyu
##  https://www.codewars.com/kata/51e0007c1f9378fa810002a9


def parse(data):
    val = 0
    final = []
    for i in data:
        if i == 'i':
            val += 1
        elif i == 'd':
            val -= 1
        elif i == 's':
            val *= val
        elif i == 'o':
            final.append(val)
            
    return final