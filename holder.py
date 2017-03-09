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

    return list(set(output))

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


GRAPH = [(1, 1), (1, 2), (2, 3), (3, 4), (4,4)]
EDGELABELS = {(1, 1): '\n\na,b', (1, 2): 'a', (2, 3): 'b', (3, 4): 'a', (4,4): '\n\na,b'}

plt.clf()


plt.clf()
#print(GRAPH)
#print(EDGELABELS)
DG = nx.DiGraph(GRAPH)
ax = plt.gca()
# pos=nx.spring_layout(DG)

pos = {}
for i in range(1, 4+1):
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
plt.savefig('x' + str(1) + '.png')
# #####################################################################################################################

# Constructing set of edges and table for nodes to edges
distinctEdges = list(set([EDGELABELS[k] for k in EDGELABELS]))
print(distinctEdges)
for i in range(len(distinctEdges)):
    if len(distinctEdges[i]) > 1:
        x = "".join(distinctEdges[i].split("\n"))
        x = x.split(",")
        distinctEdges.pop(i)
        distinctEdges.extend(x)

distinctEdges = list(set(distinctEdges))
print("Distinct Edges:", distinctEdges)

NumberOfNodes = 4 # Taken as user input

StrippedEdgeLabels = {}

for k in EDGELABELS:
    x = "".join(EDGELABELS[k].split("\n")).split(",")
    StrippedEdgeLabels[k] = x

print(StrippedEdgeLabels)

referenceTable = {}

for i in range(1,NumberOfNodes+1):
    for j in distinctEdges:
        nodesConnectedTo = [k[1] for k in StrippedEdgeLabels if k[0] == i and j in StrippedEdgeLabels[k]]
        referenceTable[(i,j)] = nodesConnectedTo

print(referenceTable)

# Initialization of final table
FinalTable = {}
currentKeys = [[1]]

for i in distinctEdges:
    FinalTable[(1, i)] = referenceTable[(1,i)]

print(FinalTable)

while True:
    localListOfNewNodes = checkNewNodes()
    if localListOfNewNodes == []:
        break
    for i in localListOfNewNodes:
        for j in distinctEdges:
            FinalTable[(tuple(sorted(i)),j)] = sorted(connectionValues(i, j))


print("FINAL TABLE")
for i in FinalTable:
    print(i, FinalTable[i])







