##  Dubstep
##  Retired
##  https://www.codewars.com/kata/551dc350bf4e526099000ae5


def song_decoder(s):
    while 'WUB' in s:
        s = s.replace('WUB',' ')
    return ' '.join([i for i in s.split(' ') if i != ''])