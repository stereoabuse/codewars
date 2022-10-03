##  Data Reverse
##  6 kyu
##  https://www.codewars.com/kata/569d488d61b812a0f7000015


def data_reverse(data):
    return sum([data[x:x+8] for x in range(0, len(data), 8)][::-1], [])