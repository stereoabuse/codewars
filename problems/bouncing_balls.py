##  Bouncing Balls
##  6 kyu
##  https://www.codewars.com/kata/5544c7a5cb454edb3c000047


def bouncingBall(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    views = 1
    while h * bounce > window:
        views += 2
        h *= bounce
    return views