##  Pete, the baker
##  5 kyu
##  https://www.codewars.com//kata/525c65e51bf619685c000059


def cakes(recipe, available):
    return 0 if not all([item in available for item in recipe]) else min({i : available[i]//recipe[i] for i in recipe}.values())