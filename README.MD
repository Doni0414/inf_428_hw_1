# Day 1: 
I have finished the task 1. Solved 3 problems from leetcode and drawed the explanation
# Day 2: 
I have finished the task 2. Aggregated the common threat score by taking mean of threat scores of users for
each department and summed the importance * mean_threat_score for each department. After divided the sum
by sum of all importance. Created 10 test cases to check that calculated threat score is within the (0, 90)
interval
# Day 3: 
I have finished task 3. Observed that simple solution exists with (hour2 - hour1) mod 24 formula. Trying to solve it with trigonometric method

## Run elastic search:
docker run --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e "xpack.security.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:8.10.0
