##  Transportation on vacation 
##  8 kyu
##  https://www.codewars.com/kata/568d0dd208ee69389d000016


def rental_car_cost(d):
    fee = 40
    if d >= 7:
        return d * fee - 50
    if d >= 3:
        return d * fee - 20
    return d * fee