##  Is he gonna survive?
##  8 kyu
##  https://www.codewars.com/kata/59ca8246d751df55cc00014c


def hero(bullets, dragons):
    if bullets // dragons >= 2:
        return True
    return False