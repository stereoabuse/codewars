##  Isograms
##  7 kyu
##  https://www.codewars.com/kata/54ba84be607a92aa900000f1


def is_isogram(string):
    for index, letter in enumerate(string):
        if letter.lower() in string.lower()[index+1:]:
            return False
    return True
            