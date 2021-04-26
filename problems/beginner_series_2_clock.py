##  Beginner Series #2 Clock
##  8 kyu
##  https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a


def past(h, m, s):
    hours = h * 60 * 60 * 1000
    minutes = m * 60 * 1000
    seconds = s * 1000
    return hours + minutes + seconds
