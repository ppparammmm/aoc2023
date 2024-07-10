def parse_cube_string(cube_string):
    """Parses a string like '3 blue' into a tuple ('blue', 3)."""
    num, color = cube_string.split()
    return color, int(num)

def load_games_from_file(file_path):
    """Loads games from a given file and returns them as a dictionary."""
    games = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                game_id, subsets = line.strip().split(':')
                game_id = int(game_id.strip().split()[1])
                subsets = [subset.strip() for subset in subsets.split(';')]
                games[game_id] = subsets
    return games

def find_minimum_cubes(game):
    """Finds the minimum number of cubes required to make a game possible."""
    min_cubes = {"red": 0, "green": 0, "blue": 0}
    
    for subset in game:
        cubes = subset.split(", ")
        for cube_string in cubes:
            color, num = parse_cube_string(cube_string)
            if num > min_cubes[color]:
                min_cubes[color] = num
    
    return min_cubes

def calculate_power(cubes):
    """Calculates the power of a set of cubes."""
    return cubes["red"] * cubes["green"] * cubes["blue"]

# Load the games from the file
file_path = r'C:\Users\a\Documents\aoc2023\day 2\input.txt'
games = load_games_from_file(file_path)

# Calculate the sum of the power of the minimum sets of cubes for each game
total_power = 0
for game in games.values():
    min_cubes = find_minimum_cubes(game)
    power = calculate_power(min_cubes)
    total_power += power

# Print the result
print(total_power)
