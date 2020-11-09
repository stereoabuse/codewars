##  Maximum subarray sum
##  5 kyu
##  https://www.codewars.com//kata/54521e9ec8e60bc4de000d6c


def max_sequence(arr):
    return_list = [0]
    for end in range(len(arr)):
        for start in range(end):
            return_list.append(sum(arr[start:end+1]))
    if sorted(return_list, reverse=True)[0] <= 0:
        return 0
    return sorted(return_list, reverse=True)[0]