import time
from rich import print

def get_data(file_path: str):
    file_data = []
    with open(file_path, 'r') as f:
        file_data = f.readlines()

    file_data = [line.strip() for line in file_data]

    return file_data



def main(file_path):
    data = get_data(file_path)
    print(data)



if __name__ == '__main__':
    file_path = str(input('File Path:\n>>> '))

    start_time = time.perf_counter()

    main(file_path)

    end_time = time.perf_counter()

    elapsed_time = end_time - start_time

    print(f'Run Time: {elapsed_time // 60}m {elapsed_time%60}s')