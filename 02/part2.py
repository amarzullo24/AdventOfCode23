# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes.
TH_RED = 12
TH_GREEN = 13
TH_BLUE = 14

def power_minumum_set(rounds):
    reds = []
    blues = []
    greens = []

    for round in rounds:
        for cube in round.split(','):
            _, quantity, color = cube.split(' ')
            quantity = int(quantity)

            if color == 'red':
                reds.append(quantity)
            elif color == 'green':
                greens.append(quantity)
            elif color == 'blue':
                blues.append(quantity)
            else:
                print("error!")
                raise Exception('color not found')
    return max(reds) * max(blues) * max(greens)
            

res = 0
with open('input.txt') as fin:
    for line in fin:
        line = line.strip()
        game, rounds = line.split(':')
        # retrienve the game ID
        gameID = game.split(' ')[-1]
        # retrieve the number of cubes for each game
        res += power_minumum_set(rounds.split(';'))

print("Answer:", res)