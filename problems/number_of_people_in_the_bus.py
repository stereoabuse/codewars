##  Number of People in the Bus
##  7 kyu
##  https://www.codewars.com/kata/5648b12ce68d9daa6b000099


def number(bus_stops):
    # Good Luck!
    people_on_bus = 0
    for stop in bus_stops:
        people_on_bus += stop[0]
    for stop in bus_stops:
        people_on_bus -= stop[1]
    return people_on_bus