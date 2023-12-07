from turtle import st


seeds = []
seeds_to_soil = {'vals': []}
soil_to_ferilizer = {'vals': []}
fertilizer_to_water = {'vals': []}
water_to_light = {'vals': []}
light_to_temperature = {'vals': []}
temperature_to_humidity = {'vals': []}
humidity_to_location = {'vals': []}

is_reading_map = False
with open('input.txt') as fin:
    for line in fin:
        line = line.strip()

        if 'seeds:' in line:
            seeds = line.split('seeds:')[-1].split(' ')[1:]
            continue
        elif 'seed-to-soil' in line:
            is_reading_map = True
            current_map = seeds_to_soil
            continue
        elif 'soil-to-fertilizer' in line:
            is_reading_map = True
            current_map = soil_to_ferilizer
            continue
        elif 'fertilizer-to-water' in line:
            is_reading_map = True
            current_map = fertilizer_to_water
            continue
        elif 'water-to-light' in line:
            is_reading_map = True
            current_map = water_to_light
            continue
        elif 'light-to-temperature' in line:
            is_reading_map = True
            current_map = light_to_temperature
            continue
        elif 'temperature-to-humidity' in line:
            is_reading_map = True
            current_map = temperature_to_humidity
            continue
        elif 'humidity-to-location' in line:
            is_reading_map = True
            current_map = humidity_to_location
            continue
        elif line == '':
            continue

        if is_reading_map:
            end, start, n = line.split(' ')
            current_map['vals'].append((int(start), int(end), int(n)))

def find_mapping(val, map):
    res = val
    for start, end, n in map['vals']:
        if val >= start and val <= start + n:
            #print('found', val, 'between', start, 'and', start + n, '. replacing with', end, '+', f'({start}-{end})', end + (val - start))
            res = end + (val - start)
            break
    return res

def find_location(seed):
    soil = find_mapping(seed, seeds_to_soil)
    fertilizer = find_mapping(soil, soil_to_ferilizer)
    water = find_mapping(fertilizer, fertilizer_to_water)
    light = find_mapping(water, water_to_light)
    temperature = find_mapping(light, light_to_temperature)
    humidity = find_mapping(temperature, temperature_to_humidity)
    location = find_mapping(humidity, humidity_to_location)
    return location

min_location = 2**30
for seed in seeds:
    seed = int(seed)
    min_location = min(find_location(seed), min_location)

print("Answer:", min_location)
        
