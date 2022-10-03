##  Are You Playing Banjo?
##  8 kyu
##  https://www.codewars.com/kata/53af2b8861023f1d88000832


def areYouPlayingBanjo(name):
    return f'{name} plays banjo' if name[0].lower() == 'r' else f'{name} does not play banjo'