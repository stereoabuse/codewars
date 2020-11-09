##  Human Readable Time
##  5 kyu
##  https://www.codewars.com//kata/52685f7382004e774f0001f7


def make_readable(seconds):
    hours = str(seconds // 3600)
    minutes = str(seconds % 3600 // 60)
    seconds = str(seconds % 3600 % 60)
    if len(hours) < 2:
        hours = "0"+hours
    if len(minutes) < 2:
        minutes = "0"+minutes
    if len(seconds) < 2:
        seconds = "0"+seconds
    return f'{hours}:{minutes}:{seconds}'