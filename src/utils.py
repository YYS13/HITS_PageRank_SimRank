from src.graph import *
import numpy as np
import time


def create_graph(data_path, transaction_case):
    gragh = Graph()
    with open(data_path) as file:
        if transaction_case:
            for line in file:
                [ignore, parent, child] = line.split()
                gragh.link(parent, child)
        else:    
            for line in file:
                [parent, child] = line.strip().split(",")
                gragh.link(parent, child)
    
    return gragh

def HITS(graph, iter):
    start = time.time()
    for i in range(iter):
        graph.HITS_update()
    end = time.time()
    exe_time = end - start
    auth = np.round(np.asarray([node.authority for node in graph.nodes]), 3)
    hub = np.round(np.asarray([node.hub for node in graph.nodes]), 3)
    return auth, hub, exe_time
    
def pageRank(graph, iter):
    start = time.time()
    graph.sort_nodes()
    graph.init_pagerank(len(graph.nodes))
    for i in range(iter):
        graph.pagerank_update()
    end = time.time()
    exe_time = end - start
    return np.round(np.asarray([node.pagerank for node in graph.nodes]), 3), exe_time

def simRank(graph, iter):
    start = time.time()
    graph.init_sim()
    for i in range(iter):
        graph.simRank_update()
    end = time.time()
    exe_time = end - start
    return np.round(np.asarray(graph.sim_matrix), 3), exe_time