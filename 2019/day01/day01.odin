package main

import "core:fmt"
import "core:os"
import "core:strconv"
import "core:strings"


Opcode :: enum int {
	Add       = 1,
	Mult      = 2,
	Terminate = 99,
}

Instruction_Width :: 4

Instruction :: struct {
	opcode:      Opcode,
	operand1:    int,
	operand2:    int,
	destination: int,
}

main :: proc() {
	data := GetInput("day01.txt")
	instruction_set := GetInstructionSet(data)
	fmt.println(data)

	input: Instruction
	start: int = 0
	debug: string

	instruction_loop: for start < len(instruction_set) - 1 {

		debug = ""


		// TODO: This is ugly: in switch as well, doing GetOpcode twice, etc
		if GetOpcode(instruction_set[start]) == Opcode.Terminate {
			debug = "Terminate"
			break instruction_loop
		}

		input = Instruction {
			opcode      = GetOpcode(instruction_set[start]),
			operand1    = instruction_set[start + 1],
			operand2    = instruction_set[start + 2],
			destination = instruction_set[start + 3],
		}

		#partial switch input.opcode {
		case Opcode.Add:
			instruction_set[input.destination] =
				instruction_set[input.operand1] + instruction_set[input.operand2]
			debug = "Add"
		case Opcode.Mult:
			instruction_set[input.destination] =
				instruction_set[input.operand1] * instruction_set[input.operand2]
			debug = "Mult"
		}


		fmt.printf(
			"\n\nstart: %d\nopcode: %d\n op1: %d\n op2: %d\ndest: %d\ndebug: %s\n",
			start,
			input.opcode,
			input.operand1,
			input.operand2,
			input.destination,
			debug,
		)

		for el in instruction_set {
			fmt.println(el)
		}
		start += Instruction_Width
	}

	// Answer
	fmt.printf("Answer: %d", instruction_set[0])
}


GetInput :: proc(file: string) -> string {
	data, err := os.read_entire_file_from_path(file, context.allocator)
	if err != nil {
		fmt.println("Could not read file")
		return ""
	}
	defer delete(data, context.allocator)

	return strings.clone(strings.trim(string(data), "\n"))
}

GetInstructionSet :: proc(data: string) -> [dynamic]int {
	instruction_set := [dynamic]int{}
	// defer delete(instruction_set)

	for value, i in strings.split(data, ",") {
		intval, ok := strconv.parse_int(value)
		if !ok {
			fmt.printf("Could not convert %d:%s input to int\n", i, value)
			return nil
		}
		append(&instruction_set, intval)
	}

	return instruction_set
}

GetOpcode :: proc(value: int) -> Opcode {
	switch value {
	case 1:
		return Opcode.Add
	case 2:
		return Opcode.Mult
	case 99:
		return Opcode.Terminate
	case:
		fmt.printf("Unsupported Opcode(%d) found, exiting\n", value)
		return Opcode.Terminate
	}
}
