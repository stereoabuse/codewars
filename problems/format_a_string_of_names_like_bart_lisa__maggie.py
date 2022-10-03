##  Format a string of names like 'Bart, Lisa & Maggie'.
##  Retired
##  https://www.codewars.com/kata/53368a47e38700bd8300030d


def namelist(names):
    names = [i['name'] for i in names]
    if len(names) <= 0:
        return ''
    elif len(names) == 1:
        return names[0]
    elif len(names) == 2:
        return f'{names[0]} & {names[1]}'
    else:
        return ', '.join(names[:-1]) + ' & ' + names[-1]