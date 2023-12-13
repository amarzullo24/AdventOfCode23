values = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}

def eval(cards):
    c_set = sorted(set(c for c in cards))
    counts = sorted([(c, cards.count(c)) for c in c_set], key=lambda x: x[-1], reverse=True)

    for c, count in counts:
        if count == 5:
            return 6
        if count == 4:
            return 5
        if count == 3:
            for c2, count2 in counts:
                if count2 == 2 and c2 != c:
                    return 4
            return 3
        if count == 2:
            for c2, count2 in counts:
                if count2 == 2 and c2 != c:
                    return 2
            return 1
    return 0

def compare(hand1, hand2):
    h1,p1 = hand1
    h2,p2 = hand2

    score1 = eval(h1)
    score2 = eval(h2)

    if score1 > score2:
        return -1
    elif score2 > score1:
        return 1
    elif score1 == score2:
        for c1,c2 in zip(h1, h2):
            if values[c1] > values[c2]:
                return -1
            elif values[c2] > values[c1]:
                return 1
    return -1

def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if compare(arr[j], arr[j + 1]) < 0:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            return
        
hands = []        
with open('input.txt') as fin:
    for line in fin:
        line = line.strip()
        hands.append(line.split(' '))

bubbleSort(hands)

res = sum(int(s[-1]) * (int(r) + 1) for r,s in enumerate(hands))
print(res)

        