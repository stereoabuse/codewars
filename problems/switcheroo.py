##  Switcheroo
##  7 kyu
##  https://www.codewars.com/kata/57f759bb664021a30300007d


def switcheroo(s):
    ans = ''
    for character in s:
        if character == 'a':
            ans += 'b'
        elif character == 'b':
            ans += 'a'
        else:
            ans += character
    return ans