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




GRAPH = [(1, 2), (2, 1), (1, 3), (1, 4), (4,3)]
EDGELABELS = {(1, 2): 'a', (1, 3): 'a', (1, 4): 'c', (2, 1): 'b', (4,3): 'f'}

plt.clf()
DG = nx.DiGraph(GRAPH)
ax = plt.gca()
# pos=nx.spring_layout(DG)

pos = {}
for i in range(1,5+1):
    pos[i] = [i,0]

draw_FA(DG,pos,ax)

for k in EDGELABELS:
    standardOffset = 0.4
    coordinatePosition = float((k[0]+k[1])/2)
    ax.annotate(EDGELABELS[k], xy=(k[0], 0), xytext=(coordinatePosition, float((k[0]-k[1])*standardOffset)))


ax.plot([1],[-0.22],marker=r'$\circlearrowleft$',ms=25)
ax.annotate('b', xy=(1, 0), xytext=(0.95, -0.50))


ax.autoscale()
plt.axis('equal')
plt.axis('off')
plt.savefig('x' + str(1) + '.png')







'''
if __name__ == "__main__":
    NumberOfNodes = int(input("ENTER THE NUMBER OF NODES IN NFA:"))

    print("**ENTER -1,-1 TO COMPLETE INSERTION OF NODES AND EDGES**")
    GRAPH = [(1, 2), (2, 1), (1, 3), (3, 4)]
    EDGELABELS = {(1, 2): 'a', (1, 3): 'a', (3, 4): 'c', (2, 1): 'b'}


    while True:
        print("ENTER A PAIR OF NODES: e.g. 1,2 ")
        nodeConnections = tuple(int(x.strip()) for x in input().split(','))
        if nodeConnections == (-1, -1):
            break
        GRAPH.append(nodeConnections)
        print("ENTER EDGE WEIGHT ON THIS PAIR: e.g. a or a,b")
        edgeWeight = input()
        if nodeConnections[0] == nodeConnections[1]:
            edgeWeight = "\n\n" + edgeWeight
        EDGELABELS[nodeConnections] = edgeWeight


    print(list(sorted(GRAPH)))
    print(EDGELABELS)
'''








