##  Categorize New Member
##  7 kyu
##  https://www.codewars.com//kata/5502c9e7b3216ec63c0001aa


def openOrSenior(data):
    newlist = []
    for item in data:
        if item[0] > 54 and item[1] > 7:
            newlist.append("Senior")
        else:
            newlist.append("Open")
    return newlist