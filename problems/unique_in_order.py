##  Unique In Order
##  6 kyu
##  https://www.codewars.com/kata/54e6533c92449cc251001667


def unique_in_order(iterable):
    r=[]
    for index, letter in enumerate(iterable):
        try:
            if letter != iterable[index+1]:
                r.append(letter)
        except: IndexError('index')
    if len(iterable) > 0:
        r.append(iterable[-1])
    return r
        