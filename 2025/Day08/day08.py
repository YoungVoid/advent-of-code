import math
import time


point_connected_to_points_dict = {}

def get_data(file_path: str) -> list[list[int]]:
    file_data = []
    with open(file_path, 'r') as f:
        file_data = f.readlines()

    file_data = [line.strip() for line in file_data]

    data = []
    for line in file_data:
        x, y, z = line.split(',')
        data.append([int(x), int(y), int(z)])

    return data

# def get_distance(position_1: list[int], position_2: list[int]) -> float:
#     return math.sqrt((position_1[0] - position_2[0])**2 + (position_1[1] - position_2[1])**2 + (position_1[2] - position_2[2])**2)

def get_distance(points_list: list[list[int]]) -> float:
    position_1, position_2 = points_list
    return math.sqrt((position_1[0] - position_2[0])**2 + (position_1[1] - position_2[1])**2 + (position_1[2] - position_2[2])**2)

def print_point_combo_list(point_combo_list):
    i = 0
    for point_combo in point_combo_list:
        i+=1
        print(f'{i} \t {point_combo}')

def build_connected_dict(line) -> dict:

    for start_point, end_point in line:
        start_point = ','.join([str(c) for c in start_point])
        end_point = ','.join([str(c) for c in end_point])

        if start_point not in point_connected_to_points_dict.keys():
            point_connected_to_points_dict[start_point] = [start_point, end_point]

        elif end_point not in point_connected_to_points_dict[start_point]:
            point_connected_to_points_dict[start_point].append(end_point)

        
        if end_point not in point_connected_to_points_dict.keys():
            point_connected_to_points_dict[end_point] = [end_point, start_point]

        elif start_point not in point_connected_to_points_dict[end_point]:
            point_connected_to_points_dict[end_point].append(start_point)
    
    return point_connected_to_points_dict

def add_points_to_circuit(circuit, points, exclude_points, connected_points_dict):
    for point in points:
        if point not in exclude_points:
            circuit.append(point)
            exclude_points.append(point)
            add_points_to_circuit(circuit, connected_points_dict[point], exclude_points, connected_points_dict)


def build_circuit(connected_points: dict) -> list[list[str]]:
    circuits = []
    points_done = []
    for start_point, points in connected_points.items():
        if start_point in points_done:
            continue

        new_circuit = []
        add_points_to_circuit(new_circuit, points, points_done, connected_points)


        circuits.append(new_circuit)
    
    return circuits

def build_connected_points_list(data: list[list[int]]) -> list[list[list[int]]]:

    connected_points_list = []

    for i in range(len(data)):
        for j in range(i+1, len(data)):
            connected_points_list.append([data[i], data[j]])
    
    return connected_points_list


def main(file_path: str):

    data = get_data(file_path)

    connected_points_list = build_connected_points_list(data)

    sorted_by_distance_list = sorted(connected_points_list,key=get_distance)

    circuits = []
    closest_count = 1000 if len(sorted_by_distance_list) >= 1000 else 10
    while len(circuits) != 1:
        if closest_count > len(sorted_by_distance_list):
            print('Couldnt find it')
            return
        
        closest_list = sorted_by_distance_list[0: closest_count]

        connections_dict = build_connected_dict(closest_list)

        circuits = build_circuit(connections_dict)

        closest_count += 1

    last_circuit = closest_list[-1][-1]
    second_last_circuit = closest_list[-1][-2]

    x1, y1, z1 = last_circuit
    x2, y2, z2 = second_last_circuit

    answer = int(x1) * int(x2)

    print(answer)

    
if __name__ == '__main__':
    file_path = str(input('File Path:\n>>> '))

    start_time = time.perf_counter()

    main(file_path)

    end_time = time.perf_counter()

    elapsed_time = end_time - start_time

    print(f'Run Time: {elapsed_time // 60}m {elapsed_time%60}s')