##  The Office VI - Sabbatical
##  7 kyu
##  https://www.codewars.com//kata/57fe50d000d05166720000b1


def sabb(s, v, h):
    total = [1 for c in s if c in "sabticl"]

    return 'Sabbatical! Boom!' if (sum(total) + v + h) > 22 else 'Back to your desk, boy.'