def parse_cube_string(cube_string):
    """Parses a string like '3 blue' into a tuple ('blue', 3)."""
    num, color = cube_string.split()
    return color, int(num)

def is_game_possible(game, max_cubes):
    """Determines if a game is possible given the maximum number of cubes."""
    for subset in game:
        cubes = subset.split(", ")
        for cube_string in cubes:
            color, num = parse_cube_string(cube_string)
            if num > max_cubes[color]:
                return False
    return True

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

# Define the maximum number of cubes of each color
max_cubes = {"red": 12, "green": 13, "blue": 14}

# Load the games from the file
file_path = r'C:\Users\a\Documents\aoc2023\day 2\input.txt'
games = load_games_from_file(file_path)

# Calculate the sum of the IDs of the possible games
possible_game_ids = [game_id for game_id, game in games.items() if is_game_possible(game, max_cubes)]
sum_of_possible_game_ids = sum(possible_game_ids)

# Print the result
print(sum_of_possible_game_ids)
