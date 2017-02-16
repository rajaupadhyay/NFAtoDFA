import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import write_dot # PYGRAPHVIZ

def draw_graph(graph, labels, numberofnodes):
    # create directed networkx graph
    G = nx.DiGraph()

    # add edges
    G.add_edges_from(graph)

    # graph_pos = nx.spring_layout(G)

    graph_pos = {}
    for i in range(1,numberofnodes+1):
        graph_pos[i] = [i,0]


    # draw nodes, edges and labels
    nx.draw_networkx_nodes(G, graph_pos, node_size=1000, node_color='blue', alpha=0.3)
    # we can now added edge thickness and edge color
    nx.draw_networkx_edges(G, graph_pos, width=2, alpha=0.3, edge_color='green')
    nx.draw_networkx_labels(G, graph_pos, font_size=12, font_family='sans-serif')

    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=labels)

    # write_dot(G, "grid.dot")
    # show graph
    plt.show()


# Define nodes and edges (user input)
if __name__ == "__main__":
    print("\n")
    for x in range(80):
        print("x",end="")
    print("\n")
    print("*".ljust(1,' ') +"NFA TO DFA CONVERTER".center(78) + "*".rjust(1,' '))
    print("*".ljust(1,' ') +"(Raja Upadhyay)".center(78) + "*".rjust(1,' '))
    print("*".ljust(1,' ') +"This program helps convert NFA Machines to DFA Machines.".center(78) + "*".rjust(1,' '))
    print("*".ljust(1,' ') +"Nodes should be NUMBERS and edges can be NUMS/CHARS.".center(78) + "*".rjust(1,' '))
    print("*".ljust(1,' ') +"Enter all connected nodes one pair at a time.".center(78) + "*".rjust(1,' '))
    print("*".ljust(1,' ') +"Pair of connected nodes are entered in the following format _,_ e.g. 5,6".center(78) + "*".rjust(1,' '))
    print("*".ljust(1,' ') +"This shows that there is and edge from node 5 to node 6".center(78) + "*".rjust(1,' '))
    print("*".ljust(1,' ') +"After each pair of nodes entered, input the edge weight between these nodes.".center(78) + "*".rjust(1,' '))
    print("*".ljust(1,' ') +"These weights can be entered as single NUMS/CHARS or multiple e.g. a,b".center(78) + "*".rjust(1,' '))
    print("*".ljust(1,' ') +"E.G. if node 1 and node 2 have an edge weight of a,b, then this means that ".center(78) + "*".rjust(1,' '))
    print("*".ljust(1,' ') +"if on node 1 we encounter an a or b then we move on to node 2.".center(78) + "*".rjust(1,' '))
    print("*".ljust(1,' ') +"Self Loops are treated as edges from the node to itself e.g. 4,4".center(78) + "*".rjust(1,' '))
    print("*".ljust(1,' ') +"ENTER -1,-1 AS PAIR OF NODES TO TERMINATE ENTRY OF NFA NODES AND EDGES".center(78) + "*".rjust(1,' '))
    for x in range(80):
        print("x", end="")
    print("\n")



    NumberOfNodes = int(input("ENTER THE NUMBER OF NODES IN NFA:"))

    print("**ENTER -1,-1 TO COMPLETE INSERTION OF NODES AND EDGES**")
    GRAPH = []
    EDGELABELS = {}

    while True:
            print("ENTER A PAIR OF NODES: e.g. 1,2 ")
            nodeConnections = tuple(int(x.strip()) for x in input().split(','))
            if nodeConnections == (-1,-1):
                break
            GRAPH.append(nodeConnections)
            print("ENTER EDGE WEIGHT ON THIS PAIR: e.g. a or a,b")
            edgeWeight = input()
            if nodeConnections[0] == nodeConnections[1]:
                edgeWeight = "\n\n" + edgeWeight
            EDGELABELS[nodeConnections] = edgeWeight

    draw_graph(GRAPH, EDGELABELS, NumberOfNodes)

    # print(GRAPH)
    # print(EDGELABELS)










