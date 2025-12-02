from rich import print


def get_data(file_path: str) -> list[str]:
    data = []
    file_line = str()
    
    with open(file_path) as f:
        file_line = f.readline()

    data = [range.split('-') for range in file_line.split(',')]
    return data


def is_valid_number(number_string:str) -> bool:
    if len(number_string) & 1 == 1:
        return True
    
    
    halfwayPos = len(number_string) // 2
    firstPart = number_string[0:halfwayPos]
    secondPart = number_string[halfwayPos:]

    if firstPart == secondPart:
        return False
    
    return True

def main(file_path):
    
    data = get_data(file_path)
  
    answer = 0

    for range_from, range_to in data:
        for number in range(int(range_from), int(range_to)+1):
            if not is_valid_number(str(number)):
                answer += number
    
    

    print(f"Answer: {answer}")
    


if __name__ == '__main__':
    file_path = str(input('File Path:\n>>> '))
    main(file_path)