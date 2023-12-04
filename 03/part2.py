import numpy as np

matrix = []
with open('input.txt') as fin:
    for line in fin:
        matrix.append(list(line.strip()))

matrix = np.asarray(matrix)

rows, cols = len(matrix), len(matrix[0])
numbers = [str(c) for c in list(range(10))]

def is_number(c):
    return c in numbers

def is_gear(c):
    return c == '*'

def clear(matrix, row, start_col, end_col):
    matrix[row, start_col:end_col] = '.'

def contains_gear(submatrix):
    for ii in range(submatrix.shape[0]):
        for jj in range(submatrix.shape[1]):
            if is_gear(submatrix[ii,jj]):
                return True, ii, jj
    return False, None, None

gear_map = {}
i = 0
while i < rows:
    j = 0
    while j < cols:
        if is_number(matrix[i][j]):
            start_col = j
            while j < cols and is_number(matrix[i][j]):
                j += 1
            end_col = min(j, cols)
            
            i_min, i_max, j_min, j_max = max(i-1,0), min(i+1+1,rows-1), max(start_col-1,0), min(end_col+1,cols)
            submatrix = matrix[i_min:i_max, j_min:j_max]

            check, gear_i, gear_j = contains_gear(submatrix)
            if check:
                key = str(gear_i + i_min) + '_' + str(gear_j + j_min)
                if not key in gear_map:
                    gear_map[key] = {'num': 0, 'vals': []}
                gear_map[key]['num'] += 1
                gear_map[key]['vals'].append(int(''.join(matrix[i,start_col:end_col])))
            #clear(matrix, i, start_col, end_col)
            j = end_col-1
        
        j += 1
    i += 1

res = 0
for key in gear_map:
    if gear_map[key]['num'] == 2:
        ratio = 1
        for val in gear_map[key]['vals']:
            ratio *= val
        
        if ratio != 1:
            res += ratio

print("The answer is", res)