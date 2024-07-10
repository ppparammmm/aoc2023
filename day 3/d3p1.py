def is_part_number(schematic, row, col):
    """Checks if a number at a specific position is a part number."""
    symbols = "*#+$"
    if not (0 <= row < len(schematic) and 0 <= col < len(schematic[row])):
        return False

    # Check all adjacent positions (including diagonals)
    for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        r, c = row + dr, col + dc
        if 0 <= r < len(schematic) and 0 <= c < len(schematic[r]) and schematic[r][c] in symbols:
            return True
    return False

def calculate_part_sum(schematic):
    """Calculates the sum of all part numbers in the schematic."""
    total_sum = 0
    for row in range(len(schematic)):
        for col in range(len(schematic[row])):
            if schematic[row][col].isdigit() and is_part_number(schematic, row, col):
                total_sum += int(schematic[row][col])
    return total_sum

# Read schematic from file
file_path = r"C:\Users\a\Documents\aoc2023\day 3\input.txt"
with open(file_path, 'r') as file:
    schematic = file.read()

# Calculate the sum of part numbers
part_sum = calculate_part_sum(schematic.splitlines())
print("Sum of all part numbers:", part_sum)
