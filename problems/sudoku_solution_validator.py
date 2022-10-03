##  Sudoku Solution Validator
##  4 kyu
##  https://www.codewars.com/kata/529bf0e9bdf7657179000008


def valid_solution(puzz):
    s = set(range(1,10))
    # squares
    top_left = set([puzz[i][j]  for j in range(3) for i in range(3)]) == s
    top_center = set([puzz[i][j]  for j in range(3,6) for i in range(3)]) == s
    top_right = set([puzz[i][j]  for j in range(6,9) for i in range(3)]) == s
    center_left =  set([puzz[i][j]  for j in range(3) for i in range(3,6)]) == s
    center_center = set([puzz[i][j]  for j in range(3,6) for i in range(3,6)]) == s
    center_left = set([puzz[i][j]  for j in range(6,9) for i in range(3,6)]) == s
    bottom_left = set([puzz[i][j]  for j in range(3) for i in range(6,9)]) == s
    bottom_center = set([puzz[i][j]  for j in range(3,6) for i in range(6,9)]) == s
    bottom_left = set([puzz[i][j]  for j in range(6,9) for i in range(6,9)]) == s
    squares = all([top_left, top_center, top_right, center_left, center_center, center_left, bottom_left, bottom_center, bottom_left])
    # rows
    rows = []
    for i in range(9):
        row = [puzz[i][j] for j in range(9)]
        rows.append(set([item for item in row]) == s)
    rows = all(rows)
    # columns
    columns = []
    for j in range(9):
        column = [puzz[i][j] for i in range(9)]
        columns.append(set([item for item in column]) == s)
    columns = all(columns)
    return columns and rows and squares
    
