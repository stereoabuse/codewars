##  Reversed Words
##  8 kyu
##  https://www.codewars.com//kata/51c8991dee245d7ddf00000e


def reverseWords(str):
    s = str.split()
    return ' '.join(s[::-1])