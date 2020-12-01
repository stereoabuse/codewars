##  WeIrD StRiNg CaSe
##  6 kyu
##  https://www.codewars.com//kata/52b757663a95b11b3d00062d


def to_weird_case(string):
    s, ans = string.split(' '), []
    for item in s:
        ans.append(''.join([char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(item)]))
    return ' '.join(ans)