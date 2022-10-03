##  Write Number in Expanded Form
##  6 kyu
##  https://www.codewars.com/kata/5842df8ccbd22792a4000245


def expanded_form(num):
    ans = []
    l = len(str(num)) -1
    for i in str(num):
        if str(i) == '0':
            l -= 1
            continue
        ans.append(str(i) + '0'*l)
        l -= 1
    return ' + '.join(ans)