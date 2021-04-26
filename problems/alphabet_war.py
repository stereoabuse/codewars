##  Alphabet war
##  7 kyu
##  https://www.codewars.com/kata/59377c53e66267c8f6000027


def alphabet_war(fight):
    l = dict(zip('wpbs', range(4,0,-1)))
    r = dict(zip('mqdz', range(4,0,-1)))
    left, right = 0,0
    for char in fight:
        if char in l:
            left += l[char]
        elif char in r:
            right += r[char]
    if left > right:
        return 'Left side wins!'
    elif right > left:
        return 'Right side wins!'
    return "Let's fight again!"