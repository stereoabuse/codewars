##  Reverse words
##  7 kyu
##  https://www.codewars.com/kata/5259b20d6021e9e14c0010d4


def reverse_words(text):
    wlr = [word[::-1] for word in text.split()]
    return "  ".join(wlr) if text.count(" ")>=len(wlr) else " ".join(wlr)