##  Filter Long Words
##  7 kyu
##  https://www.codewars.com/kata/5697fb83f41965761f000052


def filter_long_words(sentence, n):
    return [word for word in sentence.split() if len(word) > n]