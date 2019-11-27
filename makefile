mean:
	make rm
	yarn jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -input /repository/movielens/ratings.csv -output intro-to-hadoop/output-movielens-04 -file ./meanMapper.py -mapper meanMapper.py -file ./meanReducer.py -reducer meanReducer.py -file ./movies.csv

rm:
	-hdfs dfs -rm -r intro-to-hadoop/output-movielens-04
    
median:
	make rm
	yarn jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -input /repository/movielens/ratings.csv -output intro-to-hadoop/output-movielens-04 -file ./medianMapper.py -mapper medianMapper.py -file ./medianReducer.py -reducer medianReducer.py -file ./movies.csv
    
stdev:
	make rm
	yarn jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -input /repository/movielens/ratings.csv -output intro-to-hadoop/output-movielens-04 -file ./stdevMapper.py -mapper stdevMapper.py -file ./stdevReducer.py -reducer stdevReducer.py -file ./movies.csv
    
most:
	make rm
	yarn jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -input /repository/movielens/ratings.csv -output intro-to-hadoop/output-movielens-04 -file ./mostRatingMapper.py -mapper mostRatingMapper.py -file ./mostRatingReducer.py -reducer mostRatingReducer.py -file ./movies.csv
    
result:
	hdfs dfs -ls intro-to-hadoop/output-movielens-04/
	hdfs dfs -cat intro-to-hadoop/output-movielens-04/part-00000
