"""
solution ispired by https://github.com/hyper-neutrino/
All rights reserved
"""

with open('input.txt') as fin:
    seed_line, *blocks = fin.read().split('\n\n')

seed_line = list(map(int, seed_line.split(':')[-1].split()))
seeds = []
for i in range(0,len(seed_line),2):
    seeds.append((seed_line[i], seed_line[i] + seed_line[i+1]))

for block in blocks:
    ranges = []
    # now I have a list of tuples (left, right, len)
    for line in block.splitlines()[1:]:
        line = list(map(int, line.split()))
        ranges.append(line)

    # now I have to map the seed into the block
    new_ranges = []
    while len(seeds) > 0:
        start, end = seeds.pop(0)

        check = False
        for a, b, c in ranges:
            overlap_start = max(start, b)
            overlap_end = min(end, b + c)
            if overlap_start < overlap_end:
                new_ranges.append((overlap_start - b + a, overlap_end - b + a))
                if overlap_start > start:
                    seeds.append((start, overlap_start))
                if end > overlap_end:
                    seeds.append((overlap_end, end))
                
                check = True
                break
        
        if not check:
            new_ranges.append((start, end))

    seeds = new_ranges
    
print(min(seeds)[0])
            
                


