import numpy as np 
class Graph:
    def __init__(self) -> None:
        self.nodes = []
        self.sim_matrix = []
        self.new_sim_matrix = []
        self.decay_factor = 0.7
    
    def findNode(self, nodeName):
        #if the node already exist return it else create a new one
        for node in self.nodes:
            if node.name == nodeName:
                return node
        newNode = Node(nodeName)
        self.nodes.append(newNode)
        return newNode
    
    #link the parentNode and childNode
    def link(self, parent, child):
        parentNode = self.findNode(parent)
        childNode = self.findNode(child)
        parentNode.children.append(childNode)
        childNode.parents.append(parentNode)
        

    #normalize every node        
    def HITS_normalize(self):
        total_auth = 0.0
        total_hub = 0.0
        #caculate sum of auyhority and hub
        for node in self.nodes:
            total_auth += node.authority
            total_hub += node.hub
        #normalize
        for node in self.nodes:
            node.authority /= total_auth
            node.hub /= total_hub
    def init_pagerank(self, nodeNum):
        for node in self.nodes:
            node.pagerank /= nodeNum

    # update authority and hub of each node and normalization
    def HITS_update(self):
        self.sort_nodes()
        for node in self.nodes:
            node.update_auth()
        for node in self.nodes:
            node.update_hub()
        for node in self.nodes:
            node.authority = node.new_authority
        self.HITS_normalize()

    def normalize_pagerank(self):
        pagerank_sum = 0.0
        # caculate the sum of all pagerank
        for node in self.nodes:
            pagerank_sum += node.new_pagerank
            node.pagerank = node.new_pagerank
        #normalize pagerank
        for node in self.nodes:
            node.pagerank /= pagerank_sum
    
    def pagerank_update(self):
        nodesNum = len(self.nodes)
        for node in self.nodes:
            node.update_pagerank(0.1, nodesNum)
        self.normalize_pagerank()

    # sort the nodes
    def sort_nodes(self):
        self.nodes = sorted(self.nodes, key=lambda x: x.name)

    # initailize similarity matrix
    def init_sim(self):
        self.sort_nodes()
        for node1 in self.nodes:
            row = []
            for node2 in self.nodes:
                if node1.name == node2.name:
                    row.append(1.0)
                else:
                    row.append(0.0)
            self.sim_matrix.append(row)
            self.new_sim_matrix.append(row)

    # get index
    def get_index(self, node1):
        for idx, node in enumerate(self.nodes):
            if node1.name == node.name:
                return idx

    # caculate similarity
    def cal_sim(self, node1, node2):
        if node1.name == node2.name:
            return 1.0
        else:
            parentNodes1 = node1.parents
            parentNodes2 = node2.parents

            if (len(parentNodes2) == 0) or (len(parentNodes1) == 0):
                return 0.0
            else:
                similarity = 0.0
                for n1 in parentNodes1:
                    for n2 in parentNodes2:
                        idx1 = self.get_index(n1)
                        idx2 = self.get_index(n2)
                        similarity += self.sim_matrix[idx1][idx2]
                scale = self.decay_factor / (len(parentNodes1) * len(parentNodes2))
                node1_idx = self.get_index(node1)
                node2_idx = self.get_index(node2)
                self.new_sim_matrix[node1_idx][node2_idx] = scale * similarity
    # simRank update
    def simRank_update(self):
        for node1 in self.nodes:
            for node2 in self.nodes:
                self.cal_sim(node1, node2)
        self.sim_matrix = self.new_sim_matrix
    # print simRank
    def printSimMatrix(self):
        print(np.round(np.asarray(self.sim_matrix), 3))



class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parents = []
        self.authority = 1.0 #old authority make sure updating hub won't use new authority value
        self.hub = 1.0
        self.new_authority = 1.0 #sort updata value
        self.pagerank = 1.0 #old pagerank make sure updating hub won't use new authority value
        self.new_pagerank = 0.0

    def update_auth(self):
        sum = 0.0
        for node in self.parents:
            sum += node.hub
        self.new_authority = sum
    
    def update_hub(self):
        sum = 0.0
        for node in self.children:
            sum += node.authority
        self.hub = sum

    def update_pagerank(self, d, n):
        new_pagerank = 0.0
        for parent in self.parents:
            new_pagerank += parent.pagerank / len(parent.children)
        self.new_pagerank = d/n + (1-d) * new_pagerank

    