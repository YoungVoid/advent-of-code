
def get_data(file_path: str) -> list[str]:
    with open(file_path, 'r') as f:
        data = f.readlines()
    return [line.strip() for line in data]


def main(file_path: str):

    data = get_data(file_path)

    total = 0

    for line in data:
        line_list = list(line)

        number_string = ''
        prev_number_pos = -1
        for i in range(12):
            number = ''
            
            # when i = 0, we need last 11 to not be touched, so until pos -11. when i = 1, we need last 10 not touched, so until pos -10
            first_unavailable_pos = i-11 if i-11 < 0 else None
            working_list = line_list[prev_number_pos+1:first_unavailable_pos]
            
            number = str(max(working_list))

            prev_number_pos = line_list.index(number, prev_number_pos+1 if prev_number_pos != -1 else 0)

            number_string += number

        total += int(number_string)
    
    print(f"Total: {total}")
        
        



if __name__ == '__main__':
    file_path = str(input('File Path:\n>>> '))
    main(file_path)
