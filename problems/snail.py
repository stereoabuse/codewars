##  Snail
##  4 kyu
##  https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1


import numpy as np

def rotation(arr, ans):
    for item in arr[0]:
        ans.append(item)
    arr = np.rot90(arr[1:])
    return arr, ans

def snail(snail_map):
    if snail_map == [[]]:
        return []
    the_ans = list()
    snail_map = np.array(snail_map)
    for i in range(len(snail_map) + len(snail_map - 1)):
        snail_map, the_ans = rotation(snail_map, the_ans)
    return the_ans