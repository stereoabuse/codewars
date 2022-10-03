##  Multi-tap Keypad Text Entry on an Old Mobile Phone
##  6 kyu
##  https://www.codewars.com/kata/54a2e93b22d236498400134b


def presses(phrase):
    presses = ['1', 'ABC2', 'DEF3', 'GHI4', 'JKL5', 'MNO6', 'PQRS7', 'TUV8', 'WXYZ9', '*', ' 0', '#']
    total = 0
    for letter in phrase.upper():
        for press in presses:
            if letter in press:
                total += press.index(letter) + 1
    return total