from rich import print
import time




def get_data(file_path: str) -> list[list[int]]:
    file_data = []
    with open(file_path, 'r') as f:
        file_data = f.readlines()

    file_data = [line.strip() for line in file_data]

    data = []
    for line in file_data:
        x, y = line.split(',')
        data.append([int(x), int(y)])

    return data

def sort_by_x(data_list):
    return data_list[0] * 1000 + data_list[1]

def sort_by_y(data_list):
    return data_list[0] * 1000 - data_list[1]

def get_area(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return(abs(x2-x1)+1) * (abs(y2-y1)+1)

def main(file_path: str):

    data = get_data(file_path)

    # sorted_by_x = sorted(data, key=sort_by_x)
    
    # sorted_by_y = sorted(data, key=sort_by_y)

    # print(sorted_by_x)
    # print('---')
    # print(sorted_by_y)
    
    points = []
    area = 0
    for i in range(len(data)):
        for j in range(i, len(data)):
            tmp_area = get_area(data[i], data[j])
            if tmp_area > area:
                points.append([data[i], data[j]])
                area = tmp_area
    print(area)
    



if __name__ == '__main__':
    file_path = str(input('File Path:\n>>> '))

    start_time = time.perf_counter()

    main(file_path)

    end_time = time.perf_counter()

    elapsed_time = end_time - start_time

    print(f'Run Time: {elapsed_time // 60}m {elapsed_time%60}s')
