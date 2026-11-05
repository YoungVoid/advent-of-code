from rich import print

def get_number_of_digits_per_line(list_of_number_list: list[list[str]]) -> int:
    number_of_digits_per_line = 0
    for list_of_numbers in list_of_number_list:
        number_of_digits_per_line = max(number_of_digits_per_line, len(''.join(list_of_numbers)))
    return number_of_digits_per_line

def get_list_with_numbers_equal_size(list_of_number_list: list[list[str]], number_of_digits_per_number: int, number_of_columns: int) -> list[list[str]]:
    equal_size_numbers = []
    for list_of_numbers in list_of_number_list:
        number = ''.join(list_of_numbers)
        new_list = []
        pos = 0
        for i in range(number_of_columns):
            new_list.append(number[pos:pos+number_of_digits_per_number])
            pos+=number_of_digits_per_number
        equal_size_numbers.append(new_list)
    
    return equal_size_numbers

def get_reversed_numbers_and_list(list_of_number_list: list[list[str]]) -> list[list[str]]:
    reversed_numbers_and_list = []
    for list_of_numbers in list_of_number_list:
        new_list = [num[::-1] for num in list_of_numbers]
        reversed_numbers_and_list.append(new_list)
    #reversed_numbers_and_list = reversed_numbers_and_list[::-1]

    return reversed_numbers_and_list

def get_exploded_numbers(list_of_number_list: list[list[str]]) -> list[list[str]]:
    exploded_numbers = []
    for list_of_numbers in list_of_number_list:
        new_list = []
        for num in list_of_numbers:
            new_list.append(list(num))
        exploded_numbers.append(new_list)

    return exploded_numbers

def get_zipped_exploded_numbers(list_of_number_list: list[list[str]]) -> list[list[str]]:
    zipped_exploded_numbers = []
    for list_of_numbers in list_of_number_list:
        zipped_exploded_numbers.append(list(zip(*list_of_numbers)))

    return zipped_exploded_numbers

def get_formatted_numbers(list_of_number_list: list[list[str]]) -> list[list[int]]:
    formatted_numbers = []
    for list_of_numbers in list_of_number_list:
        new_list = []
        for num in list_of_numbers:
            new_list.append(int(''.join(num).replace('-','')))
        formatted_numbers.append(new_list)

    return formatted_numbers

def group_numbers(list_of_number_list: list[list[str]]) -> list[list[str]]:
    new_list1 = []
    for col_i in range(len(list_of_number_list[0])):
        new_list2 = []
        for row_i in range(len(list_of_number_list)):
            new_list2.append(list_of_number_list[row_i][col_i])
        new_list1.append(new_list2)
    return new_list1

def get_data(file_path: str) -> tuple[list[list[int], list[str]]]:
    with open(file_path, 'r') as f:
        file_data = f.readlines()

    valid_calcs = {'*','+'}

    numbers = [[num.strip() if num not in ['','\n'] else '-' for num in line.split(' ')] for line in file_data[:-1]]
    operators = [op for op in file_data[-1].split(' ') if op in valid_calcs]
    start_of_column_positions = [i for i in range(len(file_data[-1])) if file_data[-1][i] not in [' ','\n']]

    numbers = []
    for i in range(len(file_data[:-1])):
        numbers_on_line = []
        line = file_data[i]
        col_num = 0

        while col_num < len(start_of_column_positions):
            operator_pos = start_of_column_positions[col_num]
            next_operator_pos = start_of_column_positions[col_num+1] if col_num+1 < len(start_of_column_positions) else None

            next_blank_col_pos = next_operator_pos - 1 if next_operator_pos else None
            
            number = line[operator_pos:next_blank_col_pos].replace('\n','')
            
            numbers_on_line.append(number)
            col_num += 1

        numbers.append(numbers_on_line)


    reversed_numbers_and_list = get_reversed_numbers_and_list(numbers)

    grouped_numbers = group_numbers(reversed_numbers_and_list)

    exploded_numbers = get_exploded_numbers(grouped_numbers)

    zipped_exploded_numbers = get_zipped_exploded_numbers(exploded_numbers)

    formatted_numbers = get_formatted_numbers(zipped_exploded_numbers)
    
    return formatted_numbers, operators

def calculate(list_of_number_list: tuple[int], operator: str) -> int:
    if operator == '*':
        total = 1
    else:
        total = 0

    for number in list_of_number_list:
        if operator == '*':
            total *= number
        elif operator == '+':
            total += number
    return total

def main(file_path: str):

    numbers, operators = get_data(file_path)

    total = 0

    for num_list_i in range(len(numbers)):
        list_of_number_list = numbers[num_list_i]
        operator = operators[num_list_i]

        total += calculate(list_of_number_list, operator)


    print(total)



if __name__ == '__main__':
    file_path = str(input('File Path:\n>>> '))
    main(file_path)
