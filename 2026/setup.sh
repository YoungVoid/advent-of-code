#!/usr/bin/env bash
set -e

if [[ "$1" == "" ]] then 
	echo "Need a name: ie \`./setup.sh day01\`"
	exit 1
fi

day=${1,,}
day_num=${day:3:2}
day_num_no_lead_zeroes=$(echo "$day_num" | sed 's/^0*//') # non-bash way, but makes more sense for me
year=2025
echo $day_num_no_lead_zeroes

echo "Setting up $day"

mkdir -p ./$day/

cp ./templates/template.odin ./$day/$day.odin
sed -i "1s/dayxx/$day/" ./$day/$day.odin 

cp ./templates/build.sh ./$day/build.sh

if [[ -f "./input/$day.input" ]] then
	cp ./input/$day.input ./$day/$day.input
else

	echo "Fetching details from adventofcode.com"
	# not worth getting the page, since we need to login to give first part answer to get second part, so either need to manually do or script a way to update the md. Instead, just going to open the page in the browser automatically at the end of script.
	# curl https://adventofcode.com/$year/day/$day_num_no_lead_zeroes > ./$day/$day.md
	curl -H "Cookie: $(cat ./aoc-auth.secret)" https://adventofcode.com/$year/day/$day_num_no_lead_zeroes/input > ./input/$day.input

	if [[ $(cat ./$day/$day.input) == "Puzzle inputs differ by user.  Please log in to get your puzzle input." ]] then
		echo "Failed to get input, cookie invalid"
	fi

	cp ./input/$day.input ./$day/$day.input
fi

echo "Setup finished, opening browser page and Neovim"

cd $day

# Open page in browser
brave https://adventofcode.com/$year/day/$day_num_no_lead_zeroes

# Open Neovim with the main file and the input file open side by side
nvim -O2 $day.odin $day.input
