##  Opposites Attract
##  8 kyu
##  https://www.codewars.com/kata/555086d53eac039a2a000083


def lovefunc( flower1, flower2 ):
    return False if abs(flower1 - flower2) % 2 == 0 else True
