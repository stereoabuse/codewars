# Pandemia
# 7 kyu


def infected(s):
    if not "1" in s:
        return 0
    infected = 0
#     pop = len(s.replace('X',''))
    conts = [i for i in s.split('X')]
    for cont in conts:
        if '1' in cont:
            infected += len(cont)
        
    return infected/(len(s.replace('X',''))) * 100