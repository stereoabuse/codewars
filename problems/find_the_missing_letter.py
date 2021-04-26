##  Find the missing letter
##  6 kyu
##  https://www.codewars.com/kata/5839edaa6754d6fec10000a2


def find_missing_letter(chars):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chars = sorted(chars)
    minimum, maximum = letters.find(chars[0]), letters.find(chars[-1])
    for i in letters[minimum:maximum]:
        if i not in chars:
            return i
    