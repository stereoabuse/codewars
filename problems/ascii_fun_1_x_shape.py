##  ASCII Fun #1: X- Shape
##  6 kyu
##  https://www.codewars.com/kata/5906436806d25f846400009b


def x(n):
    white, black = '■', '□'
    matrix = [[black] * n for _ in range(n)]
    for ring in range(n - 1):
        matrix[0 + ring][0 + ring] = white
        matrix[n-1 - ring][n - 1 - ring] = white
        matrix[0 + ring][n - 1 - ring] = white
        matrix[n - 1 - ring][0 + ring] = white

    return '\n'.join(''.join(row) for row in matrix)