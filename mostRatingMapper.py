#!/usr/bin/env python
import sys
import csv
import json
from operator import itemgetter  
# for nonHDFS run
movieFile = "./movies.csv"

# # for HDFS run
# movieFile = "./movies.csv"

movieList = {}
userList = {}

with open(movieFile, mode = 'r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        movieList[row[0]] = {}
        movieList[row[0]]["genre"] = row[2]

for oneMovie in sys.stdin:
    oneMovie = oneMovie.strip()
    ratingInfo = oneMovie.split(",")
    mID = ratingInfo[1]
    genres = movieList[mID]["genre"].split("|")
    try:
        user = int(ratingInfo[0])
        if user in userList:
            userList[user]["count"] += 1
            for genre in genres:
                if genre in userList[user]:
                    userList[user][genre] += 1
                else:
                    userList[user][genre] = 1

        else:
            userList[user] = {}
            userList[user]["count"] = 1
            for genre in genres:
                userList[user][genre] = 1
    except ValueError:
        continue

for user in userList:
    print("%s\t%s\t%s" %(user, userList[user]["count"], userList[user]))

