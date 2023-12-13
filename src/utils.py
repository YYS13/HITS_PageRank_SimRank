from src.graph import *


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
    for i in range(iter):
        graph.HITS_update()
    print([node.authority for node in graph.nodes])
    print([node.hub for node in graph.nodes])
    
def pageRank(graph, iter):
    for i in range(iter):
        graph.pagerank_update()
    print([node.pagerank for node in graph.nodes])

def simRank(graph, iter):
    graph.init_sim()
    for i in range(iter):
        graph.simRank_update()
    graph.printSimMatrix()