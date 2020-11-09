##  Build a pile of Cubes
##  6 kyu
##  https://www.codewars.com//kata/5592e3bd57b64d00f3000047


def find_nb(m):
    cubes = 1
    cube_vol = 1
    while True:
        if cube_vol >= m:
            break
        cubes += 1
        cube_vol += cubes ** 3
    if cube_vol == m:
        return cubes
    return -1