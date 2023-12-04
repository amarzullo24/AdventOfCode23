def preprocess(card):
     # let's remove the "Card X: " string
    card = card.split(':')[-1][1:]
    # divide the extracted numbers from the played numbers
    extracted, played = card.split('|')
    # convert into a list of
    extracted, played = extracted.split(' '), played.split(' ')
    # remove extra blank characters
    extracted, played = [e for e in extracted if e != ''], [p for p in played if p != '']
    return extracted, played
    
def solve(card):
    extracted, played = preprocess(card)
    matches = 0
    for p in played:
        if p in extracted:
            matches += 1
    return pow(2, matches - 1) if matches != 0 else matches

points = 0
with open('input.txt') as fin:
    for line in fin:
        points += solve(line.strip())

print("The answer is:", points)