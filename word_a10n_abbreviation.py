##  Word a10n (abbreviation)
##  6 kyu
##  https://www.codewars.com//kata/5375f921003bf62192000746


import re
def abbreviate(s):
    s_list = re.split('([\W\d_])', s)
    end_list = []
    for i in s_list:
        if i:
            if len(i) >= 4:
                end_list.append(f'{i[0]}{len(i)-2}{i[-1]}')
            elif len(i) < 4:
                end_list.append(i)
    return ''.join(end_list)