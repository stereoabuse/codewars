##  List Filtering
##  7 kyu
##  https://www.codewars.com/kata/53dbd5315a3c69eed20002dd


def filter_list(l):
    return list(filter(lambda x:type(x) == int, l))