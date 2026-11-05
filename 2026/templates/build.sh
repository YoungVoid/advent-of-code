#!/usr/bin/env bash
set -e

runtests=false
runmain=false
testfile="test.input"
if [[ "$1" == "run" ]] then
	if [[ "$2" == "test" ]] then
		runtests=true
	elif [[ "$2" == "main" ]] then
		runmain=true
	elif [[ "$2" == "all" ]] then
		runtests=true
		runmain=true
	fi
fi

if [[ "$3" != "" ]] then
	testfile=$3
fi

# Assuming the current directory has the day's name
day=${PWD##*/}

odin build . -debug

if [[ $runtests == true ]] then
	./$day testfile
fi

if [[ $runmain == true ]] then
	./$day $day.input
fi



