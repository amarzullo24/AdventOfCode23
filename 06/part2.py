
with open('input.txt') as fin:
    distances, records = fin.readlines()
    distances = [int("".join(distances.split()[1:]))]
    records = [int("".join(records.split()[1:]))]

wins = 1
check = False
for d,r in zip(distances, records):
    win = 0
    ms = 0
    while(ms < d):
        mm = ms * (d - ms)
        if mm > r:
            win += 1
            check = True
        ms += 1
    
    if win != 0:
        wins *= win

res = wins if check else 0
print(res)