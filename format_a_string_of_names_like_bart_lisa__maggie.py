##  Format a string of names like 'Bart, Lisa & Maggie'.
##  6 kyu
##  https://www.codewars.com//kata/53368a47e38700bd8300030d


def namelist(names):
    namelist = [i['name'] for i in names]
    if len(namelist) > 2:
        return ', '.join(namelist[:-1]) + ' & ' + namelist[-1]
    if len(namelist) == 2:
        return ' & '.join(namelist)
    if len(namelist) == 1:
        return namelist[0]
    if len(namelist) == 0:
        return ""
    
    