from rich import print

def get_data(file_path: str) -> list[list[int]]:
    with open(file_path, 'r') as f:
        data = f.readlines()

    blank_line_position = data.index('\n')

    fresh_range_data = [[int(num) for num in line.strip().split('-')] for line in data[0:blank_line_position]]

    return fresh_range_data


def main(file_path: str):

    fresh_range_data = get_data(file_path)
    fresh_range_data.sort()

    total = 0
    previous_end = 0

    for range_list in fresh_range_data:
        include_start = True
        start, end = range_list
        start = max(start, previous_end)

        if start > end:
            continue

        if start <= previous_end:
            include_start = False
            start = previous_end

        total += (end-start) + (1 if include_start else 0)
        previous_end = end

    print(total)



if __name__ == '__main__':
    file_path = str(input('File Path:\n>>> '))
    main(file_path)
