#!/usr/bin/env python
import sys
import csv
import json

current_genre = None
current_rating_sum = 0
current_rating_count = 0
current_rating_list = []

for line in sys.stdin:
    line = line.strip()
    genre, rating = line.split("\t", 1)

    if current_genre == genre:
        try:
            current_rating_list.append(float(rating))
        except ValueError:
            continue    
    else:
        if current_genre:
            current_rating_list = current_rating_list.sort()
            median = current_rating_list[len(current_rating_list)/2]
            print ("%s\t%s" % (current_genre, median))    
        current_genre = genre
        try:
            current_rating_list.append(float(rating))
        except ValueError:
            continue

if current_genre == genre:
    current_rating_list = current_rating_list.sort()
    median = current_rating_list[len(current_rating_list)/2]
    print ("%s\t%s" % (current_genre, median)) 