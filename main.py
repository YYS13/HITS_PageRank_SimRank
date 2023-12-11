import os
from src.utils import *

data_path = os.getcwd() + "/inputs/"
files = ["graph_1.txt", "graph_2.txt", "graph_3.txt", "graph_4.txt", "graph_5.txt", "graph_6.txt"]
#create 7 graphs(graph_1, graph_2, graph_3, graph_4, graph_5, graph_6, graph_7)
for file in files:
    if file[:3] == "gra":
        globals()[file[:7]] = create_graph(data_path + file)
    else:
        globals()[file[:3]] = create_graph(data_path + file)
