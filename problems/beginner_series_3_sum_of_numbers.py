##  Beginner Series #3 Sum of Numbers
##  7 kyu
##  https://www.codewars.com//kata/55f2b110f61eb01779000053


def get_sum(a,b):
    if a == b:
        return a
    elif a < b:
        return sum([i for i in range(a, b+1)])
    elif b < a:
        return sum([i for i in range(b, a+1)])