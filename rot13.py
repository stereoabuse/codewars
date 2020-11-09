##  Rot13
##  5 kyu
##  https://www.codewars.com//kata/530e15517bc88ac656000716


def rot13(message):
    import string
    newstring = ""
    for character in message:
        if character in string.ascii_lowercase[:13]:
            newstring += string.ascii_lowercase[13:][string.ascii_lowercase[:13].index(character)]
        elif character in string.ascii_lowercase[13:]:
            newstring += string.ascii_lowercase[:13][string.ascii_lowercase[13:].index(character)]
        elif character in string.ascii_uppercase[:13]:
            newstring += string.ascii_uppercase[13:][string.ascii_uppercase[:13].index(character)]
        elif character in string.ascii_uppercase[13:]:
            newstring += string.ascii_uppercase[:13][string.ascii_uppercase[13:].index(character)]
        else:
            newstring += character
    return newstring
    