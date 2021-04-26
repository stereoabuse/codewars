##  Simple Pig Latin
##  5 kyu
##  https://www.codewars.com/kata/520b9d2ad5c005041100000f


def pig_it(text):
    return " ".join([(item[1:]+item[0]+'ay') if item.isalpha() else item for item in text.split()])