package main

import "core:fmt"
import "core:os"

GetInput :: proc(file: string) -> string {
	data, err := os.read_entire_file_from_path(file, context.allocator)
	return string(data)
}

main :: proc() {
	fmt.println(GetInput("day01.txt"))
}
