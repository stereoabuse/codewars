##  Stop gninnipS My sdroW!
##  6 kyu
##  https://www.codewars.com/kata/5264d2b162488dc400000001


def spin_words(sentence):
    # Your code goes here
    sent_list = sentence.split()
    new_list = []
    for item in sent_list:
        if len(item) > 4:
            item = item[::-1]
        new_list.append(item)
    return " ".join(new_list)