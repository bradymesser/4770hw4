#!/usr/bin/env python
import sys
import csv
import json


def mean(data):
    """Return the sample arithmetic mean of data."""
    n = len(data)
    if n < 1:
        raise ValueError('mean requires at least one data point')
    return sum(data)/n # in Python 2 use sum(data)/float(n)

def _ss(data):
    """Return sum of square deviations of sequence data."""
    c = mean(data)
    ss = sum((x-c)**2 for x in data)
    return ss

def stddev(data, ddof=1):
    """Calculates the population standard deviation
    by default; specify ddof=1 to compute the sample
    standard deviation."""
    n = len(data)
    if n < 2:
        raise ValueError('variance requires at least two data points')
    ss = _ss(data)
    pvar = ss/(n-ddof)
    return pvar**0.5


current_genre = None
current_rating_sum = 0
current_rating_count = 0
current_rating_list = []
data = {}

for line in sys.stdin:
    line = line.strip()
    genre, rating = line.split("\t", 1)
    if genre in data:
        data[genre].append(float(rating))
    else:
        data[genre] = []
        data[genre].append(float(rating))
for genre in data:
    print(genre,stddev(data[genre]))
