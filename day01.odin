package main

import "core:fmt"
import "core:os"
import "core:strconv"
import "core:strings"


Opcode :: enum {
	Add,
	Mult,
	Terminate,
}

Instruction_Width :: 4


main :: proc() {
	instruction_set := GetInput("day01.txt")
	for el in instruction_set {
		fmt.println(el)
	}
}


GetInput :: proc(file: string) -> [dynamic]int {
	data, err := os.read_entire_file_from_path(file, context.allocator)
	if err != nil {
		fmt.println("Could not read file")
		return nil
	}
	defer delete(data, context.allocator)


	instruction_set := [dynamic]int{}
	defer delete(instruction_set)

	for value, i in strings.split(strings.trim(string(data), "\n"), ",") {
		intval, ok := strconv.parse_int(value)
		if !ok {
			fmt.printf("Could not convert %d:%s input to int", i, value)
			return nil
		}
		append(&instruction_set, intval)
	}

	return instruction_set
}
