# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 05:23:10 2020

@author: YoungVoid
"""


def Part1():
    timestamp = 1002576
    BusList = [13, 37, 449, 29, 19, 23, 773, 41, 17]

    # timestamp = 939
    # BusList = [7,13,59,31,19]

    LeastBusid = 0
    LeastBusTime = 100000000
    for busid in BusList:
        BusNextDepartTime = busid * (timestamp // busid + 1)
        BusTimeWait = BusNextDepartTime - timestamp
        if BusTimeWait < LeastBusTime:
            LeastBusTime = BusTimeWait
            LeastBusid = busid

    return LeastBusid * LeastBusTime


def Part2():
    BusList = [
        13,
        0,
        0,
        0,
        0,
        0,
        0,
        37,
        0,
        0,
        0,
        0,
        0,
        449,
        0,
        29,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        19,
        0,
        0,
        0,
        23,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        773,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        41,
        0,
        0,
        0,
        0,
        0,
        0,
        17,
    ]
    # BusList = [7,13,59,31,19]
    # BusList = [17,0,13,19]
    BusList = [67, 7, 59, 61]
    # BusList = [67,0,7,59,61]
    # BusList = [67,7,0,59,61]
    # BusList = [1789,37,47,1889]

    maxPos = BusList.index(max(BusList))

    counter = 1
    timestampFound = False
    while not timestampFound and counter < 9999999999999999999:
        baseTimestamp = BusList[maxPos] * counter
        if baseTimestamp % 1000000 == 0:
            print(str(counter) + "\t" + str(baseTimestamp))

        BusTimes = []
        for busidCounter in range(0, len(BusList)):
            busid = BusList[busidCounter]
            if busid == 0:
                continue
            addedTimestamp = busid * (baseTimestamp // busid)
            PosOffset = busidCounter - maxPos
            if addedTimestamp - PosOffset == baseTimestamp:
                BusTimes.append(addedTimestamp)
                timestampFound = True
            else:
                timestampFound = False
                break

        counter += 1

    return BusTimes[0]


print(Part2())
