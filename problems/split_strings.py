##  Split Strings
##  6 kyu
##  https://www.codewars.com/kata/515de9ae9dcfc28eb6000001


def solution(s):
    if len(s) == 0:
        return []
    elif len(s) % 2 == 0:
        return [s[i:i+2] for i in range(0, len(s), 2)]
    elif len(s) % 2 != 0:
        listval = [s[i:i+2] for i in range(0, len(s)-1, 2)]
        listval.append(s[-1]+'_')
        return listval
        