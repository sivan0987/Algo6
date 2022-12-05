
from typing import List

import networkx as nx


def find_cycle_in_consumption_graph(allocation: List[List[float]]):
    G = nx.Graph()

    for p in range(len(allocation)):

        for o in range(len(allocation[0])):
            if  allocation[p][o] >0:
                G.add_edge(("player", p), ("object", o))
    try:
        print(list(nx.find_cycle(G, orientation="ignore")))
    except:
        print("there is no cycle")


if __name__ == '__main__':
    # G = nx.Graph()
    # G.add_node(1,2)
    # G.add_node(1, 2)
    find_cycle_in_consumption_graph([[1,0,1], [1,1,0],[0,1,1]])
    find_cycle_in_consumption_graph([[1, 0, 0], [0, 1, 0], [0, 0, 1]])