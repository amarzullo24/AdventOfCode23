def solve(line):
    if sum(line) == 0:
        return 0
    return line[-1] + solve([line[i+1] - line[i] for i in range(len(line)-1)])

with open('input.txt') as fin:
    res = 0
    for line in fin:
        line = list(map(int, line.strip().split()))
        res += solve(line)

print(res)