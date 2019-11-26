#!/usr/bin/env python
import sys
import csv
import json

current_genre = None
current_rating_sum = 0
current_rating_count = 0
current_rating_list = []
data = {}

for line in sys.stdin:
    line = line.strip()
    genre, rating = line.split("\t", 1)
    if genre in data:
        data[genre].append(rating)
    else:
        data[genre] = []
        data[genre].append(rating)
for genre in data:
    data[genre].sort()
    mid = int(len(data[genre]) / 2)
    print(genre,data[genre][mid])
