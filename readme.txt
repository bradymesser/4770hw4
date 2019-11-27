CPSC 4770/6770 Homework 4
Brady Messer and Bhavik Suthar
Fall 2019

Each program is split up into mappers and reducers, to be ran with yarn.
To run without yarn and with hdfs and one local file, use the files in
the mapReducers subdirectory, here all of the mappers and reducers are combined
into one file however they do not work with yarn.

To run with yarn use the makefile commands:
  - make mean
    - will calculate the average rating for each genre
  - make median
    - will calculate the median rating for each genre
  - make stdev
    - will calculate the standard deviation for each genre
  - make most
    - will find the user that has left the most ratings for movies and their most rated genre