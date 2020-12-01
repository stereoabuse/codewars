##  Weight for weight
##  5 kyu
##  https://www.codewars.com//kata/55c6126177c9441a570000cc


def order_weight(string):
    stringlist = [a for a in string.split(" ")]
    newlist = []
    for item in string.split(" "):
        newlist.append(sum([int(dig) for dig in item]))
    
    return " ".join([x for _,x in sorted(zip(newlist, stringlist))])
                       