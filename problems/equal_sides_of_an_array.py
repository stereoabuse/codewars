##  Equal Sides Of An Array
##  6 kyu
##  https://www.codewars.com//kata/5679aa472b8f57fb8c000047


def find_even_index(arr):
    for i in range(len(arr)):
        try:
            if sum(arr[:i]) == sum(arr[i + 1:]):
                if i == 0:
                    return 0
                return i
        except:
            IndexError
    return -1
        
    