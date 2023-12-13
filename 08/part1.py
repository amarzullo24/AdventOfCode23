from collections import defaultdict 

intructions = None
graph = defaultdict(list)

with open('input.txt') as fin:
    for i, row in enumerate(fin):
        if i == 0:
            instructions = row.strip()
        elif i == 1:
            continue
        else:
            node, children = row.strip().replace(' ', '').split('=')
            node, (child1, child2) = node, children[1:-1].split(',')

            graph[node].append(child1)
            graph[node].append(child2)

i = 0
steps = 0
q = ['AAA']

while(q):
    n = q.pop(0)
    if n == 'ZZZ':
        print(steps)
        exit()
    
    if instructions[i] == 'L':
        q.append(graph[n][0])
    else:
        q.append(graph[n][1])
    
    i = (i + 1) % len(instructions)
    steps += 1


        

