# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes.
TH_RED = 12
TH_GREEN = 13
TH_BLUE = 14

def check_rounds(rounds):
    for round in rounds:
        for cube in round.split(','):
            _, quantity, color = cube.split(' ')
            curr_th = None
            if color == 'red':
                curr_th = TH_RED
            elif color == 'green':
                curr_th = TH_GREEN
            elif color == 'blue':
                curr_th = TH_BLUE
            else:
                print("error!")
                raise Exception('color not found')
            
            if int(quantity) > curr_th:
                return True
    return False
            

res = 0
with open('input.txt') as fin:
    for line in fin:
        line = line.strip()
        game, rounds = line.split(':')
        # retrienve the game ID
        gameID = game.split(' ')[-1]
        # retrieve the number of cubes for each game
        if not check_rounds(rounds.split(';')):
            res += int(gameID)

print("Answer:", res)

                
    