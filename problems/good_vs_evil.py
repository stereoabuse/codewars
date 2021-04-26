##  Good vs Evil
##  6 kyu
##  https://www.codewars.com/kata/52761ee4cffbc69732000738


def goodVsEvil(good, evil):
    light, dark, equal = ['Good triumphs over Evil', 'Evil eradicates all trace of Good', 'No victor on this battle field']
    good_worth = [1, 2, 3, 3, 4, 10]
    evil_worth = [1, 2, 2, 2, 3, 5, 10]
    gg = sum(good_worth[index] * int(char) for index, char in enumerate(good.split()))
    ee = sum(evil_worth[index] * int(char) for index, char in enumerate(evil.split()))
    if gg > ee:
        ans = light
    elif gg < ee:
        ans = dark
    else:
        ans = equal
    return f'Battle Result: {ans}'