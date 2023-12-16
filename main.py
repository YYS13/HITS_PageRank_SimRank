import os
from src.utils import *


data_path = os.getcwd() + "/inputs/"
files = ["graph_1.txt", "graph_2.txt", "graph_3.txt", "graph_4.txt", "graph_6.txt", "ibm-5000.txt", "graph_5.txt"]
#create 7 graphs(graph_1, graph_2, graph_3, graph_4, graph_5, graph_6, graph_7)
for idx, file in enumerate(files):
    if file[:3] == "gra":
        graph = create_graph(data_path + file, False)
        authority, hub, exe_time = HITS(graph, 30)
        print(file[:7] + f" HITS time: {exe_time}s")
        np.savetxt(os.getcwd() + "/results/" + file[:7] + "/" + file[:7] + "_HITS_authority.txt", authority.reshape(1, len(authority)), fmt='%.3f')
        np.savetxt(os.getcwd() + "/results/" + file[:7] + "/" + file[:7] + "_HITS_hub.txt", hub.reshape(1, len(hub)), fmt='%.3f')
        pr, exe_time = pageRank(graph, 30)
        print(file[:7] + f" PageRank time: {exe_time}s")
        np.savetxt(os.getcwd() + "/results/" + file[:7] + "/" + file[:7] + "_PageRank.txt", pr.reshape(1, len(pr)), delimiter=' ', fmt='%.3f')
        if file[6] != '6':
            sr, exe_time = simRank(graph, 30)
            print(file[:7] + f" SimRank time: {exe_time}s")
            np.savetxt(os.getcwd() + "/results/" + file[:7] + "/" + file[:7] + "_SimRank.txt", sr, delimiter=' ', fmt='%.3f')
    else:
        graph = create_graph(data_path + file, True)
        authority, hub, exe_time = HITS(graph, 30)
        print(file[:7] + f" HITS time: {exe_time}s")
        np.savetxt(os.getcwd() + "/results/" + file[:8] + "/" + file[:8] + "_HITS_authority.txt", authority.reshape(1, len(authority)), fmt='%.3f')
        np.savetxt(os.getcwd() + "/results/" + file[:8] + "/" + file[:8] + "_HITS_hub.txt", hub.reshape(1, len(hub)), fmt='%.3f')
        pr, exe_time = pageRank(graph, 30)
        print(file[:7] + f" PageRank time: {exe_time}s")
        np.savetxt(os.getcwd() + "/results/" + file[:8] + "/" + file[:8] + "_PageRank.txt", pr.reshape(1, len(pr)), fmt='%.3f')

