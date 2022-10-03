##  Total amount of points
##  8 kyu
##  https://www.codewars.com/kata/5bb904724c47249b10000131


def points(games):
    total = 0
    for game in games:
        x, y = game.split(':')
        if int(x) > int(y):
            total += 3
        elif int(x) == int(y):
            total += 1
    return total