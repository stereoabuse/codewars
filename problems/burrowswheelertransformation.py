##  Burrows-Wheeler-Transformation
##  4 kyu
##  https://www.codewars.com/kata/54ce4c6804fcc440a1000ecb


def encode(s):
    if not s: return s, 0
    matrix = sorted([char for char in s][n:] + [char for char in s][:n] for n in range(len(s), 0, -1))
    for index, row in enumerate(matrix):
        if ''.join(row) == s:
            row_index = index
            break
    last_column = ''.join(matrix[i][-1] for i in range(len(matrix)))
    return last_column, index


def decode(s,n):
    if not s: return s
    matrix = [[] for i in range(len(s))]
    for col, char in enumerate(s):
        for index, row in enumerate(matrix):
            matrix[index].insert(0, s[index])
        matrix = sorted(matrix)
    return ''.join(matrix[n])