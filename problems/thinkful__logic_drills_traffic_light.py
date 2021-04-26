##  Thinkful - Logic Drills: Traffic light
##  8 kyu
##  https://www.codewars.com/kata/58649884a1659ed6cb000072


def update_light(current):
    if current == 'green':
        return 'yellow'
    elif current == 'yellow':
        return 'red'
    elif current == 'red':
        return 'green'
    else:
        raise "we have a problem"
