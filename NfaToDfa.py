import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Circle
import networkx as nx


def checkNewNodes():
    newNodes = []
    for i in FinalTable:
        if FinalTable[i] not in currentKeys:
            currentKeys.append(FinalTable[i])
            newNodes.append(FinalTable[i])
    return newNodes

def connectionValues(listVals, edgeWeight):
    output = []
    for i in listVals:
        output.extend(referenceTable[(i,edgeWeight)])

    return sorted(list(set(output)))

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


# GRAPH = [(1, 2), (2, 1), (1, 3), (1, 4), (4,3)]
# EDGELABELS = {(1, 2): 'a', (1, 3): 'a', (1, 4): 'c', (2, 1): 'b', (4,3): 'f'}

plt.clf()


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
    #print(GRAPH)
    #print(EDGELABELS)
    DG = nx.DiGraph(GRAPH)
    ax = plt.gca()
    # pos=nx.spring_layout(DG)

    pos = {}
    for i in range(1, NumberOfNodes + 1):
        pos[i] = [i, 0]

    draw_FA(DG, pos, ax)

    for k in EDGELABELS:
        standardOffset = 0.4
        if k[0] != k[1]:
            coordinatePosition = float((k[0] + k[1]) / 2)
            ax.annotate(EDGELABELS[k], xy=(k[0], 0), xytext=(coordinatePosition, float((k[0] - k[1]) * standardOffset)))
        else:
            ax.plot([k[0]], [-0.22], marker=r'$\circlearrowleft$', ms=25)
            ax.annotate(EDGELABELS[k], xy=(1, 0), xytext=(k[0], -0.50))

    ax.autoscale()
    plt.axis('equal')
    plt.axis('off')
    plt.savefig('NFA' + str(1) + '.png')

    # print(GRAPH)
    # print(EDGELABELS)


# *************************************************************************************************************


    # Constructing set of edges and table for nodes to edges
    distinctEdges = list(set([EDGELABELS[k] for k in EDGELABELS]))
    # print(distinctEdges)
    for i in range(len(distinctEdges)):
        if len(distinctEdges[i]) > 1:
            x = "".join(distinctEdges[i].split("\n"))
            x = x.split(",")
            distinctEdges.pop(i)
            distinctEdges.extend(x)

    distinctEdges = list(set(distinctEdges))
    # print("Distinct Edges:", distinctEdges)

    StrippedEdgeLabels = {}

    for k in EDGELABELS:
        x = "".join(EDGELABELS[k].split("\n")).split(",")
        StrippedEdgeLabels[k] = x

    # print(StrippedEdgeLabels)

    referenceTable = {}

    for i in range(1,NumberOfNodes+1):
        for j in distinctEdges:
            nodesConnectedTo = [k[1] for k in StrippedEdgeLabels if k[0] == i and j in StrippedEdgeLabels[k]]
            referenceTable[(i,j)] = nodesConnectedTo

    # print(referenceTable)

    # Initialization of final table
    FinalTable = {}
    currentKeys = [[1]]

    for i in distinctEdges:
        FinalTable[(1, i)] = referenceTable[(1,i)]

    # print(FinalTable)


    NodeList = {(1) : 1}
    ExistingNodes = []
    counter = 2
    while True:
        localListOfNewNodes = checkNewNodes()
        for i in localListOfNewNodes:
            if sorted(i) not in ExistingNodes:
                NodeList[tuple(sorted(i))] = counter
                ExistingNodes.append(sorted(i))
                counter += 1

        if localListOfNewNodes == []:
            break
        for i in localListOfNewNodes:
            for j in distinctEdges:
                FinalTable[(tuple(sorted(i)),j)] = sorted(connectionValues(i, j))

    # print(NodeList)
    # print(FinalTable)

    # PRINT HERE DERIVE GRAPH LIKE ABOVE ON LINE 52
    # NodeConnections = [(NodeList[k[0]], (FinalTable[k])) for k in FinalTable]
    NodeConnections = []
    EDGELABELS2 = {}

    for k in FinalTable:
        if len(FinalTable[k]) > 1:
            NodeConnections.append((NodeList[k[0]], NodeList[tuple(sorted(FinalTable[k]))]))
        else:
            NodeConnections.append((NodeList[k[0]],*FinalTable[k]))
        EDGELABELS2[(k[0], tuple(sorted(FinalTable[k])))] = k[1]

    # print(EDGELABELS2)

    FinalDict = {}

    for k in EDGELABELS2:
        if not isinstance(k[0], int):
            val1 = NodeList[k[0]]
        else:
            val1 = k[0]
        if len(list(k[1])) > 1:
            val2 = NodeList[k[1]]
        else:
            val2 = k[1][0]
        FinalDict[(val1, val2)] = EDGELABELS2[k]

    # INPUT GRAPH TO DRAW FUNCTION *************************************************************************************
    print(NodeConnections)

    print(FinalDict)


    plt.clf()


    #print(GRAPH)
    #print(EDGELABELS)
    DG = nx.DiGraph(NodeConnections)
    ax = plt.gca()
    # pos=nx.spring_layout(DG)

    pos = {}
    for i in range(1, len(NodeConnections)+1):
        pos[i] = [i, 0]

    draw_FA(DG, pos, ax)

    for k in FinalDict:
        standardOffset = 0.4
        if k[0] != k[1]:
            coordinatePosition = float((k[0] + k[1]) / 2)
            ax.annotate(FinalDict[k], xy=(k[0], 0), xytext=(coordinatePosition, float((k[0] - k[1]) * standardOffset)))
        else:
            ax.plot([k[0]], [-0.22], marker=r'$\circlearrowleft$', ms=25)
            ax.annotate(FinalDict[k], xy=(1, 0), xytext=(k[0], -0.50))

    ax.autoscale()
    plt.axis('equal')
    plt.axis('off')
    plt.savefig('DFA' + str(2) + '.png')

























