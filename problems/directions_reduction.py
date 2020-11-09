##  Directions Reduction
##  5 kyu
##  https://www.codewars.com//kata/550f22f4d758534c1100025a


def dirReduc(arr):
    while True:
        length = len(arr)
        try:
            for index in range(1, len(arr)):
                if (arr[index] == 'NORTH' and arr[index-1] == "SOUTH" or
                    arr[index] == 'SOUTH' and arr[index-1] == "NORTH"or
                    arr[index] == 'EAST' and arr[index-1] == "WEST" or
                    arr[index] == 'WEST' and arr[index-1] == "EAST"):
                    del arr[index-1:index+1]
            if len(arr) == length:
                return arr
        except:
            IndexError