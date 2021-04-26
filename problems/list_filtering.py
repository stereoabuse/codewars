##  List Filtering
##  7 kyu
##  https://www.codewars.com/kata/53dbd5315a3c69eed20002dd


def filter_list(l):
    """Return a new list with the strings filtered out"""
    return [i for i in l if type(i) != str]