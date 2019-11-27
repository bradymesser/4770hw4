#!/usr/bin/env python
import sys
import csv
import json
import operator 

currentCount = 0
maxCount = 0
maxUser = 0
maxGenre = None
maxvalue = 0
for line in sys.stdin:
    line = line.strip()
    user, holder = line.split("\t", 1)
    holder = holder.strip()
    count, holder2 = holder.split("\t", 1)
    string = holder2
    Dict = eval(string)
    
    currentCount = int(count)
    if maxCount < currentCount:
        maxCount = currentCount
        maxUser = user
        maxGenre = Dict
        num = (list(sorted(maxGenre.values()))[-2])
        for key, value in maxGenre.items():
            if num == value:
                maxGenrename = key
print("%s -- Total Rating Counts: %s -- Most Rated Genre: %s - %s " %(maxUser, maxCount, maxGenrename, num))
