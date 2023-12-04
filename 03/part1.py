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

def is_symbol(c):
    return not c in numbers and c != '.'

def clear(matrix, row, start_col, end_col):
    matrix[row, start_col:end_col] = '.'

def contains_symbol(submatrix):
    for ii in range(submatrix.shape[0]):
        for jj in range(submatrix.shape[1]):
            if is_symbol(submatrix[ii,jj]):
                return True
    return False

res = 0
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

            if contains_symbol(submatrix):
                res += int(''.join(matrix[i,start_col:end_col]))
            else:
                #clear(matrix, i, start_col, end_col)
                j = end_col-1
        j += 1
    i += 1

print("The answer is", res)
            
