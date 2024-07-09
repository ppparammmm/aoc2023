def find_calibration_value(line):
    # Mapping of spelled-out digits to their corresponding numeric values
    digit_words = {
        "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
        "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    # Replace spelled-out digits with their corresponding numeric values
    for word, digit in digit_words.items():
        line = line.replace(word, digit)

    # Identify the first digit
    first_digit = None
    for char in line:
        if char.isdigit():
            first_digit = char
            break
    
    # Identify the last digit
    last_digit = None
    for char in reversed(line):
        if char.isdigit():
            last_digit = char
            break
    
    # Combine the digits to form the calibration value
    if first_digit is not None and last_digit is not None:
        return int(first_digit + last_digit)
    else:
        return 0

def calculate_total_calibration(input_lines):
    total_calibration_value = 0
    for line in input_lines:
        total_calibration_value += find_calibration_value(line)
    return total_calibration_value

# Read input from file
def read_input_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

# Example usage:
file_path = r'C:\Users\a\Documents\aoc2023\day 1\inputd1p1.txt'
input_lines = read_input_file(file_path)
total_calibration_value = calculate_total_calibration(input_lines)
print(f"Total Calibration Value: {total_calibration_value}")
