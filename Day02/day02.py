from rich import print


def get_data(file_path: str) -> list[str]:
    data = []
    file_line = str()
    
    with open(file_path) as f:
        file_line = f.readline()

    data = [range.split('-') for range in file_line.split(',')]
    return data


def is_valid_number(number_string:str) -> bool:
    # if len(number_string) == 0:
    #     return True
    
    is_whole_string_repeating = False
    
    for split_count in range(2, len(number_string)+1):
        if len(number_string) % split_count != 0:
            continue

        is_whole_string_repeating = False

        for split_counter in range(split_count-1):
            split_length = len(number_string) // split_count
            split_start = split_length * (split_counter)
            firstPart = number_string[0:split_length]
            CompareVal1 = number_string[split_start:split_start+split_length]
            CompareVal2 = number_string[split_start+split_length:split_start+split_length*2]

            if firstPart == CompareVal1 and CompareVal1 == CompareVal2:
                is_whole_string_repeating = True
            else:
                is_whole_string_repeating = False
                break
        if is_whole_string_repeating:
            break
    
    return not is_whole_string_repeating 

def main(file_path):
    
    data = get_data(file_path)
  
    answer = 0

    for range_from, range_to in data:
        for number in range(int(range_from), int(range_to)+1):
            if not is_valid_number(str(number)):
                print(number)
                answer += number
    
    

    print(f"Answer: {answer}")
    


if __name__ == '__main__':
    file_path = str(input('File Path:\n>>> '))
    main(file_path)