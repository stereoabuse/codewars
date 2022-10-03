##  Framed Reflection
##  6 kyu
##  https://www.codewars.com/kata/581331293788bc1702001fa6


def mirror(text):
    text = text.split()
    length = max(len(x) for x in text)
    first, last = ['*' * length + '*' * 4] *2
    words = first + '\n' + '\n'.join([f'* {word[::-1].ljust(length, " ")} *' for word in text]) + '\n' + last
    return words