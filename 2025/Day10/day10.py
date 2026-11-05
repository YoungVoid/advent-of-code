from dis import get_instructions
import time
from rich import print
from itertools import permutations

def get_data(file_path: str):
    file_data = []
    with open(file_path, 'r') as f:
        file_data = f.readlines()

    file_data = [line.strip() for line in file_data]

    data = []
    for line in file_data:
        lights, *buttons, joltage = line.split(' ')
        data.append([lights, buttons, joltage])

    return data

def get_light_bools(light_requirement:str):
    light_bools = []
    for character in light_requirement:
        if character == '.':
            light_bools.append(False)
        elif character == '#':
            light_bools.append(True)
    return light_bools

def get_instruction_result(button_sequence, light_length):
    result = [False for _ in range(light_length)]

    for button in button_sequence:
        for light_pos in map(int, button[1:-1].split(',')):
            result[light_pos] = not result[light_pos]
            
    return result

def process_instruction_line_and_get_shortest_instruction(line):
    light_requirement, buttons, joltage = line
    light_bools = get_light_bools(light_requirement)

    n = len(buttons)
    
    for r in range(1, n+1):
        button_permutation = permutations(buttons,r)
    
        for button_sequence in button_permutation:
            instruction_result = get_instruction_result(button_sequence, len(light_bools))
            if instruction_result == light_bools:
                return len(button_sequence)
    



def main(file_path):
    data = get_data(file_path)

    total = 0
    for line in data:
        total += process_instruction_line_and_get_shortest_instruction(line)

    print(total)


if __name__ == '__main__':
    file_path = str(input('File Path:\n>>> '))

    start_time = time.perf_counter()

    main(file_path)

    end_time = time.perf_counter()

    elapsed_time = end_time - start_time

    print(f'Run Time: {elapsed_time // 60}m {elapsed_time%60}s')