def preprocess(card):
     # let's split the "Card X: " string and the numbers
    cardID, card = card.split(':')
    # extract the cardID and the numbers
    cardID = cardID.split(' ')[-1]
    card = card[1:] # remove the extra space
    # divide the extracted numbers from the played numbers
    extracted, played = card.split('|')
    # convert into a list of
    extracted, played = extracted.split(' '), played.split(' ')
    # remove extra blank characters
    extracted, played = [e for e in extracted if e != ''], [p for p in played if p != '']
    return cardID, extracted, played
    
def solve(extracted, played):
    matches = []
    for p in played:
        if p in extracted:
            matches.append(str(int(game) + len(matches) + 1))
    
    return matches

counters = {}

count = 0
with open('input.txt') as fin:
    for line in fin:
        game, extracted, played = preprocess(line.strip())
        matches = solve(extracted, played)

        if not game in counters:
            counters[game] = 1
        else:
            counters[game] += 1
        
        for i in range(counters[game]):
            for match in matches:
                if not match in counters:
                    counters[match] = 1
                else:
                    counters[match] += 1

print("The answer is:", sum(counters.values()))