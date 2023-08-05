# CSPL--602006final

This project is aimed at proving the theory in Motif-based PageRank(github: https://github.com/HKUST-KnowComp/Motif-based-PageRank.git)
We make use of pettingZoo to create the similar environment according to the description in the essay "Ranking Users in Social Networks with Higher-Order Structures" for collecting the data from this environment. And we use the data to test the algorithm in Motif-based PageRank.

graph.py: make use of the data collected ftom the environment based on petting Zoo
levels.csv: data collected from petting Zoo which decides theb level of agent
main.py: code for collecting data from environment
message_history: record the sender and reciver message which makes up the citation network
reformatted_message_history: transfer the format of message_history data into algorithm format
remi_test2/remi_test3/remi_test4: simulate the petting zoo environment
