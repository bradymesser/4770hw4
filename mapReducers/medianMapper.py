#!/usr/bin/env python
import sys
import csv
import json
import statistics

# for nonHDFS run
movieFile = "./movies.csv"

# # for HDFS run
# movieFile = "./movies.csv"

movieList = {}
genreList = {}

with open(movieFile, mode = 'r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        movieList[row[0]] = {}
        movieList[row[0]]["title"] = row[1]
        movieList[row[0]]["genre"] = row[2]
        
lst = []

for oneMovie in sys.stdin:
    oneMovie = oneMovie.strip()
    ratingInfo = oneMovie.split(",")
    try:
        genres = movieList[ratingInfo[1]]["genre"]
        rating = float(ratingInfo[2])
        for genre in genres.split("|"):
            if genre in genreList:
                genreList[genre]["total_rating"] += rating
                genreList[genre]["total_count"] += 1
                genreList[genre]["ratings"].append(rating)
            else:
                genreList[genre] = {}
                genreList[genre]["total_rating"] = rating
                genreList[genre]["total_count"] = 1
                genreList[genre]["ratings"] = []
                genreList[genre]["ratings"].append(rating)

    except ValueError:
        continue
        
for genre in genreList:
    print(genre,statistics.median(genreList[genre]["ratings"]))
    
    
    
    