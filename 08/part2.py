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
qs = [[key] for key in graph if key[-1] == 'A']
q_steps = [0] * len(qs)

while(any(qs)):
    count_end = 0

    for idx, q in enumerate(qs):
        if q:
            n = q.pop(0)
            
            if n[-1] == 'Z':
                q_steps[idx] = steps
            elif instructions[i] == 'L':
                q.append(graph[n][0])
            else:
                q.append(graph[n][1])

    i = (i + 1) % len(instructions)
    steps += 1


import math
lcm = 1
for i in q_steps:
    lcm = lcm*i//math.gcd(lcm, i)
print(lcm)