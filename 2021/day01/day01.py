# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 16:36:41 2021

@author: YoungVoid

current issue:
    largerCount is returning 1601 - should be 1602
    not sure why
    initial value 127 is not counted
    last value seems to have been counted
"""


def getPuzzleInput(filename):
    with open(filename, "r") as f:
        return f.read().split("\n")


def day1part1(puzzleInputFile):
    puzzleInput = getPuzzleInput(puzzleInputFile)
    largerCount = 0
    added = " "
    previousMeasurement = puzzleInput[0]
    for currentMeasurement in puzzleInput:
        if currentMeasurement > previousMeasurement:
            largerCount += 1
            added = "Y"
        # else:
        #    print('Curr: {}\tPrev: {}\tLarger: {}'.format(currentMeasurement,previousMeasurement,largerCount))
        # print('Curr: {}\nPrev: {}\nLarger: {}'.format(currentMeasurement,previousMeasurement,largerCount))
        print(
            "Curr: {}\tPrev: {}\tLarger: {}\t{}".format(
                currentMeasurement, previousMeasurement, largerCount, added
            )
        )
        previousMeasurement = currentMeasurement

        added = " "

        # if largerCount > 8:
        #     break
    return largerCount


def main():
    filename = "testPuzzleInput.txt"
    filename = "puzzleInput.txt"
    print(getPuzzleInput(filename))
    print("Day 1 Part 1 Answer: {}".format(day1part1(filename)))


if __name__ == "__main__":
    main()
