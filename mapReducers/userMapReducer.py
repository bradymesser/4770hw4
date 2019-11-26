#!/usr/bin/env python
import sys
import csv
import json
import statistics
import operator

# for nonHDFS run
# movieFile = "./movies.csv"

# # for HDFS run
movieFile = "./movies.csv"

movieList = {}
userList = {}

with open(movieFile, mode = 'r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        movieList[row[0]] = {}
        movieList[row[0]]["genre"] = row[2]
        
lst = []

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
        
# print(userList[186590])
maxCount = 0
maxUser = 0
for user in userList:
    if userList[user]["count"] > maxCount:
        maxUser = user
        maxCount = userList[user]["count"]
        
print("Max user: ", maxUser, " Max count: ", maxCount)
print(userList[maxUser])
    
    