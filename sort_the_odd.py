##  Sort the odd
##  6 kyu
##  https://www.codewars.com//kata/578aa45ee9fd15ff4600090d


def sort_array(source_array):
    odds = sorted([x for x in source_array if x % 2 != 0])
    newlist, b = [], 0
    for item in source_array:
        if item % 2 != 0:
            newlist.append(odds[b])
            b += 1
        else:
            newlist.append(item)
    return newlist
    