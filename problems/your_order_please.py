##  Your order, please
##  6 kyu
##  https://www.codewars.com//kata/55c45be3b2079eccff00010f


def order(sentence):
    sd = dict()
    for word in sentence.split(" "):
        for character in word:
            if character.isdigit():
                sd[word] = int(character)
    return " ".join(sorted(sd, key=sd.get))
            