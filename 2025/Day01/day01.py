import math
from rich import print

def get_data(file_path: str) -> list[str]:
  data = []
  with open(file_path) as f:
    data = f.readlines()

  return data




def get_new_position(current_position: int, instruction: str) -> tuple[int, int]:
    direction = str(instruction[0])
    distance = int(instruction [1:])
    new_position = current_position
    password_increments = 0

    # Need to not count this twice - would already have been counted for in previous instruction
    if current_position == 0 and direction == 'L':
      password_increments -= 1

    if distance >= 100:
      password_increments += math.floor(distance / 100)
      distance = distance % 100 

    if direction == 'L':
      new_position -= distance
    else: 
      new_position += distance

    if new_position < 0:
      new_position += 100
      password_increments += 1
    elif new_position > 99:
      new_position -= 100
      password_increments += 1
    elif new_position == 0:
      password_increments += 1


    return new_position, password_increments




def main():
  file_path = str(input('File Path:\n>>> '))

  data = get_data(file_path)

  password = 0
  current_position = 50

  for instruction in data:
    direction = str(instruction[0])
    distance = int(instruction [1:])
    password_increments = 0

    new_position, password_increments = get_new_position(current_position, instruction)
    
    current_position = new_position
    password += password_increments

  print(f"Password: {password}")
    





if __name__ == '__main__':
  main()