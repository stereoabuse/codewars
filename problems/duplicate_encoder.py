##  Duplicate Encoder
##  6 kyu
##  https://www.codewars.com//kata/54b42f9314d9229fd6000d9c


def duplicate_encode(word):
    new = ''
    for character in word:
        if word.lower().count(character.lower()) == 1:
            new += ("(")
        else:
            new += (')')
    return new