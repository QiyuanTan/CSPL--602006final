# Project Intro:
This project is aimed at proving the theory and algorithmic feasibility in Motif-based PageRank(github: https://github.com/HKUST-KnowComp/Motif-based-PageRank.git) We make use of pettingZoo to create the similar environment according to the description in the essay "Ranking Users in Social Networks with Higher-Order Structures" for collecting the data from this environment. Furthermore, we reproduce the PageRank Algorithm Code and use the data to test its feasibility.

### Project flow:
Setting up the environment - Collecting data - Validating the algorithm - Project evaluation

### Members:
Lucy Cui, Yi Li, Eric Tan, Akaley Weng

### Project history:
Akaley Weng analyses the thesis find out necessary and tell Eric Tan what kind of environment he needs to make.
After making environment by pettingZoo, Eric Tan collect the necessary data and convert to special data forms.
YI LI use the data to test the PageRank algorithm he reproduce to test the result and create the network graph and evaluation graph based on the data given by Eric Tan
After getting results from the experiment，Lucy Cui analyses and evaluates the results of the experiment and make prepare the presentation.


### File intro:
graph.py: make use of the data collected from the environment based on petting Zoo

levels.csv: data collected from petting Zoo which decides the data level of agent

main.py: code for collecting data from environment

message_history: record the sender and reciver message which makes up the citation network

reformatted_message_history: transfer the format of message_history data into algorithm format

remi_test2/remi_test3/remi_test4: simulate the petting zoo environment


### Conrtribution:
Lucy Cui: Analyse and evaluate the results of the experiment and prepare the presentation
Yi Li: reproduce the PageRank algorithm，use the data collected provided to make different graphs
Eric Tan: create the environment by pettingZoo, collect necessary data according to requirements
Akaley Weng: analyses the thesis and find the necessary environmental elements

### Paper 
The paper: https://doi.org/10.54097/zsfnjk16 is based on this project

### Reference：
Pagerank essay can be found here:
https://aaai.org/papers/11287-ranking-users-in -social-networks-with-higher-order-structures/
Our code is accessible by:
https://github.com/QiyuanTan/CSPL-- \602006final/blob/main/main.ipynb
Pagerank code is available here:
https://github.com/HKUST-KnowComp/Motif-based-PageRank.git


