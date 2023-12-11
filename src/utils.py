from src.graph import *


def create_graph(data_path):
    gragh = Graph()
    with open(data_path) as file:
        for line in file:
            [parent, child] = line.strip().split(",")
            gragh.link(parent, child)
    
    return gragh