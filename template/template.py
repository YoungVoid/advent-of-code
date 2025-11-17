#import sys
import os
from typing import Literal
# import logging

#
# Rich setup
#
from rich import print
from rich.console import Console
from rich.traceback import install
from rich.panel import Panel
# from rich.logging import RichHandler
from rich.pretty import Pretty

# pyright: ignore[reportInvalidStringEscapeSequence] #
# Commonly used standard library imports for Advent of Code puzzles - according to google ai:
#

# This module provides powerful tools for creating efficient iterators for various combinatorial problems, 
# such as permutations, combinations, and cartesian products (product). pairwise (available in Python 3.10+) 
# is also very useful for iterating over consecutive pairs.
# import itertools 

# Offers specialized container datatypes like deque (double-ended queue), Counter (for counting hashable objects), 
# and defaultdict (for dictionaries with default values), which are frequently helpful in puzzle-solving.
# import collections

# Contains mathematical functions and constants, including gcd, lcm, sqrt, and trigonometric functions, 
# which can be relevant for number theory or geometry-based problems.
# import math

# Regex
# import re

# large arrays or Matrices
# import numpy as np

# Builds upon numpy and offers a wide range of scientific computing tools, including optimization algorithms, 
# linear algebra routines, and statistical functions, which might be useful for more complex or data-intensive puzzles.
# import scipy

# When dealing with graph-based problems (e.g., finding shortest paths, connected components), 
# networkx provides a comprehensive suite of tools for creating, manipulating, and analyzing graphs.
# import networkx as nx

# If a problem requires symbolic mathematics or solving algebraic equations, sympy can be a powerful tool.
# import sympy as sp


from dotenv import load_dotenv
load_dotenv()



r"""
  _    _      _                   ______                _   _                 
 | |  | |    | |                 |  ____|              | | (_)                
 | |__| | ___| |_ __   ___ _ __  | |__ _   _ _ __   ___| |_ _  ___  _ __  ___ 
 |  __  |/ _ \ | '_ \ / _ \ '__| |  __| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
 | |  | |  __/ | |_) |  __/ |    | |  | |_| | | | | (__| |_| | (_) | | | \__ \
 |_|  |_|\___|_| .__/ \___|_|    |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
               | |                                                            
               |_|                                                            
"""              

def color_text(text, color):
    return f"[{color}]{text}[/{color}]"


def get_default_input_path() -> str:
    """Gets the default path to the input file. Calculated as: __file__ minus extension + "_input.txt"

    Returns:
        str: The default input file path. 
    """
    return os.path.splitext(__file__)[0] + "_input.txt"


def get_input(file_path: str=get_default_input_path()) -> list[str]:
    """Read the input file (file_path) and return the data as a list

    Args:
        file_path (str, optional): The path to the input file. Defaults to get_default_input_path().

    Returns:
        list[str]: Input data as a list.
    """

    with open(file_path, 'r') as file:
        data = file.read().strip().splitlines()

    #data = [int(line) for line in data]
    console.print(Panel(Pretty(data), title="Input Data", style="bold white on blue")) if Config.PRINT_INPUT else None

    return data


def write_answer_to_file(file_path: str, answer: str) -> None:
    with open(file_path, 'w') as file:
        file.write(answer)


class Config:
    VERBOSE: bool = os.getenv("VERBOSE", "False").lower() in ("true", "1", "yes", "y")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes", "y")
    WRITE_FILE: bool = os.getenv("WRITE_FILE", "True").lower() in ("true", "1", "yes", "y")
    PRINT_INPUT: bool = os.getenv("PRINT_INPUT", "False").lower() in ("true", "1", "yes", "y")






def print_test_result(test_number: int = 0, expected: int|str|None = None, got: int|str|None = None) -> None:
    success = str(got) == str(expected) if expected is not None else None

    if success is True:
        console.print(Panel(f"{got}", title=f"Test {test_number} Passed!", style="bold white on green"))
    elif success is False:
        console.print(Panel(f"Expected: \n{expected} \n\nGot: \n{got}", title=f"Test {test_number} Failed!", style="bold white on red"))
    else:
        console.print(Panel(str(got), title=f"Test {test_number} Answer", style="bold white on green"))



def print_main_answer(answer: int|str|None) -> None:
    console.print(Panel(str(answer), title="Actual Answer", style="bold white on purple")) if Config.VERBOSE else None




def test(file_path: str, expected: int|str|None=None, test_number: int=0):
    
    data = get_input(file_path)

    answer = get_answer_part2(data) or get_answer_part1(data)

    if expected is not None:
        if str(answer) == str(expected):
            yield True #console.print(Panel(f"{answer}", title=f"Test {test_number} Passed!", style="bold white on green"))
        else:
            yield False #console.print(Panel(f"Expected: \n{expected} \n\nGot: \n{answer}", title=f"Test {test_number} Failed!", style="bold white on red"))
    else:
         yield None #console.print(Panel(str(answer), title=f"Test {test_number} Answer", style="bold white on green"))

    yield answer




r"""
  __  __       _         _      _              _____                             _             
 |  \/  |     (_)       | |    (_)            |  __ \                           (_)            
 | \  / | __ _ _ _ __   | |     _ _ __   ___  | |__) | __ ___   ___ ___  ___ ___ _ _ __   __ _ 
 | |\/| |/ _` | | '_ \  | |    | | '_ \ / _ \ |  ___/ '__/ _ \ / __/ _ \/ __/ __| | '_ \ / _` | 
 | |  | | (_| | | | | | | |____| | | | |  __/ | |   | | | (_) | (_|  __/\__ \__ \ | | | | (_| |
 |_|  |_|\__,_|_|_| |_| |______|_|_| |_|\___| |_|   |_|  \___/ \___\___||___/___/_|_| |_|\__, |
                                                                                          __/ |
                                                                                         |___/ 
"""

def format_data(data: list[str]) -> list:
    """_summary_

    Args:
        data (list[str]): _description_

    Returns:
        list: _description_
    """
    # --------------------------------

    return data

def get_answer_part1(data: list):
    """TODO:_summary_

    Args:
        data (list, optional): Input data for processing. Defaults to get_input().
    """

    data = format_data(data)

    # --------------------------------
    # TODO: Process the data as needed
    # --------------------------------

    answer = None

    return answer


def get_answer_part2(data: list):
    # TODO: Copy part1 and modify as needed
    return None









def get_answer_main(file_path: str=get_default_input_path(), part: int|None=None) -> int|str:
    """_summary_

    Args:
        file_path (str, optional): _description_. Defaults to get_default_input_path().

    Returns:
        _type_: _description_
    """
    
    data = get_input(file_path)

    if part == 1:
        answer = get_answer_part1(data) or 'Part 1 not implemented!'
    elif part == 2:
        answer = get_answer_part2(data) or 'Part 2 not implemented!'
    else:
        answer = get_answer_part2(data) or get_answer_part1(data) or 'Neither part1 nor part2 implemented!'

    return answer







def main():
    #--------------------------
    # Init
    #--------------------------
    os.system("cls" if os.name == "nt" else "clear")
    test_number = 0


    #--------------------------
    # Test Cases
    #--------------------------
    console.rule("Test Cases")

    if True:
        test_number = 1
        expected = 2
        test_input_file_path = os.path.splitext(__file__)[0] + "_input_test1.txt"
        part = None  # Set to 1 or 2 to test specific part

        try:
            answer = get_answer_main(test_input_file_path, part=part)
        except Exception:
            console.print_exception()
    
        print_test_result(test_number, expected, answer)

    #--------------------------
    # Main Run
    #--------------------------
    console.rule("Main Run")
    input_file_path = get_default_input_path()

    try:
        answer = get_answer_main(input_file_path)
        print_main_answer(answer)
    except IndexError:
        console.print_exception()
        console.print("[red]Error:[/red] Input data is empty or not properly formatted.")
    except Exception:
        console.print_exception()


    #--------------------------
    # Finalize
    #--------------------------
    console.rule("Finalize")

    if Config.WRITE_FILE:
        output_file_path = os.path.splitext(__file__)[0] + "_output.txt"
        write_answer_to_file(output_file_path, str(answer))
        console.print(f"Answer written to {color_text(output_file_path,'yellow')}")



if __name__ == "__main__":    
    install() # rich
    console = Console() # rich

    main()