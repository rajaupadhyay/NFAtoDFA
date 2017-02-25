import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Circle
import networkx as nx

def draw_FA(G, pos, ax):
    # Draw NFA/DFA
    for n in G:
        c = Circle(pos[n], radius=0.1, alpha=0.7, color='red', gid='11')
        ax.add_patch(c)
        G.node[n]['patch'] = c
        ax.text(pos[n][0]-0.05, pos[n][1]-0.04, str(n))
    seen={}
    for (u,v,d) in G.edges(data=True):
        n1 = G.node[u]['patch']
        n2 = G.node[v]['patch']
        rad = 0.7
        if (u,v) in seen:
            rad = seen.get((u,v))
            rad = (rad + np.sign(rad) * 0.1) * -1
        alpha = 0.5

        color = 'k'
        e = FancyArrowPatch(n1.center, n2.center,
                            patchA=n1, patchB=n2,
                            arrowstyle='->',
                            connectionstyle='arc3,rad=%s' % rad,
                            mutation_scale=10.0,
                            lw=2, alpha=alpha, color=color)
        seen[(u, v)] = rad
        ax.add_patch(e)

#
# GRAPH = [(1, 2), (2, 1), (1, 3), (1, 4), (4,3)]
# EDGELABELS = {(1, 2): 'a', (1, 3): 'a', (1, 4): 'c', (2, 1): 'b', (4,3): 'f'}
#
# plt.clf()

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

    plt.clf()
    DG = nx.DiGraph(GRAPH)
    ax = plt.gca()
    # pos=nx.spring_layout(DG)

    pos = {}
    for i in range(1, 5 + 1):
        pos[i] = [i, 0]

    draw_FA(DG, pos, ax)

    for k in EDGELABELS:
        standardOffset = 0.4
        if k[0] != k[1]:
            coordinatePosition = float((k[0] + k[1]) / 2)
            ax.annotate(EDGELABELS[k], xy=(k[0], 0), xytext=(coordinatePosition, float((k[0] - k[1]) * standardOffset)))
        else:
            ax.plot([k[0]], [-0.22], marker=r'$\circlearrowleft$', ms=25)
            ax.annotate(EDGELABELS[k], xy=(1, 0), xytext=(0.95, -0.50))

    ax.autoscale()
    plt.axis('equal')
    plt.axis('off')
    plt.savefig('x' + str(1) + '.png')

    # print(GRAPH)
    # print(EDGELABELS)










