##  Moving Zeros To The End
##  5 kyu
##  https://www.codewars.com//kata/52597aa56021e91c93000cb0


def move_zeros(array):
    zero_index = []
    for i, item in enumerate(array):
        if item == 0:
            if item is not False:
                zero_index.append(i)
    for j in sorted(zero_index, reverse = True):
        array.pop(j)
        array.append(0)
            
        

    return array #, zero_index, new_array