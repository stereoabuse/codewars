##  Multiplication table
##  6 kyu
##  https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08


def multiplication_table(size):
    ans = []
    for row in range(1, size+1):
        x = []
        for column in range(1, size+1):
            x.append(row * column)
        ans.append(x)
    return ans