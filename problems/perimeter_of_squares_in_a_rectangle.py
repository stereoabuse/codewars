##  Perimeter of squares in a rectangle
##  5 kyu
##  https://www.codewars.com//kata/559a28007caad2ac4e000083


def fib():
    '''Generates the fib, starting with 0'''
    x, y = 1, 1
    while 1:
        yield x
        x, y = y, x + y

def perimeter(n):
    f = fib()
    return 4 * sum([next(f) for i in range(n+1)])