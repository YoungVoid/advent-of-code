package dayxx

import "core:fmt"
import "core:os"

main :: proc() {
	inputfile: string
	if len(os.args) == 1 {
		inputfile = fmt.aprintf("%s.%s", os.args[0], "txt")
	} else if len(os.args) >= 2 {
		inputfile = os.args[1]
	}

	input := getInput(inputfile)

	// Do Stuff
	answer: int = 0

	fmt.println(input)
	fmt.println(string(input))



	fmt.printfln("Answer: %d", answer)

}

getInput :: proc(filename: string) -> []byte {
	buffer: []byte
	err: os.Error
	buffer, err = os.read_entire_file(filename, context.allocator)
	if err != nil {
		return []byte{}
	}
	return buffer
}
