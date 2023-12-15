# PART1:
matrix = []
with open('input.txt') as fin:
    si,sj = -1,-1
    for i, line in enumerate(fin):
        line = line.strip()
        subline = []
        for j, c in enumerate(line):
            if c == 'S':
                si = i
                sj = j
            subline.append(c)
        matrix.append(subline)

width = len(matrix)
height = len(matrix[0])

def fill(x,y):
    current = matrix[x][y]
    matrix[x][y] = '*'
    neighbors = None
    if current == 'F':
        neighbors = [(x+1,y),(x,y+1)]
    if current == '|':
        neighbors = [(x+1,y),(x-1,y)]
    if current == '-':
        neighbors = [(x,y+1),(x,y-1)]
    if current == 'J':
        neighbors = [(x,y-1),(x-1,y)]
    if current == 'L':
        neighbors = [(x-1,y),(x,y+1)]
    if current == '7':
        neighbors = [(x+1,y),(x,y-1)]

    count = 0
    for n in neighbors:
        if 0 <= n[0] <= width-1 and 0 <= n[1] <= height-1:
            if current == 'S':
                count += 1
            if not current in ['F', '|', '-', 'J', 'L', '7']:
                count += 0

# Everything begins:
visited = {(si,sj):'S'}

q = [(si-1,sj),(si+1,sj),(si,sj-1),(si,sj+1)]
count = 0
while q:
    (x,y) = q.pop(0)
    current = matrix[x][y]
    
    if current == 'S' or not current in ['F', '|', '-', 'J', 'L', '7']:
        continue

    if (x,y) in visited:
        continue

    visited[(x,y)] = matrix[x][y]

    count += 1

    neighbors = []
    if current == 'F':
        neighbors = [(x+1,y),(x,y+1)]
    if current == '|':
        neighbors = [(x+1,y),(x-1,y)]
    if current == '-':
        neighbors = [(x,y+1),(x,y-1)]
    if current == 'J':
        neighbors = [(x,y-1),(x-1,y)]
    if current == 'L':
        neighbors = [(x-1,y),(x,y+1)]
    if current == '7':
        neighbors = [(x+1,y),(x,y-1)]

    for n in neighbors:
        if 0 <= n[0] <= width-1 and 0 <= n[1] <= height-1:
            q.append((n[0],n[1]))

# Property:
# assuming to have an irregular shape and you want to know if a point is inside the shape or not
# for each point x,y imagine to draw a ray in any direction
# if the ray crosses the boundary an odd number of times then the point is "in"
# assuming drawing a ray in the low-right diagonal (to avoid traversing borders)
# exclude "tangent" cases (L,7)

def expand_ray(matrix, x, y):
    count = 0
    i,j = x,y
    while i < len(matrix) and j < len(matrix[0]):
        if (i,j) in visited and not visited[(i,j)] in "L7":
            count += 1
        i += 1
        j += 1
    return count


count = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if not (i,j) in visited:
            cross = expand_ray(matrix, i, j)
            if cross % 2 == 1:
                count += 1

print(count)

#for line in matrix:
#    print("".join(l for l in line))

            