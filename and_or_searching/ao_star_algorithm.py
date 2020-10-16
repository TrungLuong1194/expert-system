import networkx as nx
import matplotlib.pyplot as plt

costs = {'n0': 0, 'n1': 2, 'n2': 4, 'n3': 4, 'n4': 6, 'n5': 1, 'n6': 2, 'n7': 0, 'n8': 0}
goalNodes = ['n7', 'n8']


def makeG(mg):
    for i in mg.nodes:
        mg.nodes[i]['solved'] = False
        mg.nodes[i]['cost'] = costs[i]

    for i in mg.edges:
        mg[i[0]][i[1]]['marked'] = False
        mg[i[0]][i[1]]['andby'] = None


def cost(mg, node):
    return nx.get_node_attributes(mg, 'cost')[node]


def solved(mg, node):
    return nx.get_node_attributes(mg, 'solved')[node]


def andby(mg, edge1, edge2):
    return nx.get_edge_attributes(mg, 'andby')[edge1, edge2]


def marked(mg, edge1, edge2):
    return nx.get_edge_attributes(mg, 'marked')[edge1, edge2]


def findleaf(g):
    for i in g.nodes:
        if not g.__getitem__(i):
            if i not in goalNodes:
                return i

    return None


def addToG(n, nodeList):
    for i in nodeList:
        # print(i)
        if not g.has_edge(n, i):
            g.add_edge(n, i, marked=False, andby=andby(mainGraph, n, i))
            g.nodes[i]['cost'] = cost(mainGraph, i)
            g.nodes[i]['solved'] = False
            if i in goalNodes:
                g.nodes[i]['solved'] = True


def findMin(q, m):
    ls = []
    MinNode = min(q, key=q.get)
    ls.append(MinNode)
    if andby(g, m, MinNode):
        ls.append(andby(g, m, MinNode))

    return ls


mainGraph = nx.DiGraph()
startNode = 'n0'

edges = [
    ('n0', 'n1'),
    ('n0', 'n4'),
    ('n0', 'n5'),
    ('n1', 'n3'),
    ('n2', 'n4'),
    ('n2', 'n5'),
    ('n2', 'n3'),
    ('n3', 'n5'),
    ('n3', 'n6'),
    ('n4', 'n5'),
    ('n4', 'n8'),
    ('n5', 'n7'),
    ('n5', 'n8'),
    ('n6', 'n7'),
    ('n6', 'n8')
]

mainGraph.add_edges_from(edges)
makeG(mainGraph)

mainGraph.edges['n0', 'n4']['andby'] = 'n5'
mainGraph.edges['n0', 'n5']['andby'] = 'n4'
mainGraph.edges['n2', 'n4']['andby'] = 'n5'
mainGraph.edges['n2', 'n5']['andby'] = 'n4'
mainGraph.edges['n3', 'n5']['andby'] = 'n6'
mainGraph.edges['n3', 'n6']['andby'] = 'n5'
mainGraph.edges['n5', 'n7']['andby'] = 'n8'
mainGraph.edges['n5', 'n8']['andby'] = 'n7'
mainGraph.edges['n6', 'n7']['andby'] = 'n8'
mainGraph.edges['n6', 'n8']['andby'] = 'n7'

nx.draw_networkx(mainGraph)
plt.show()

g = mainGraph.subgraph(startNode).copy()

if startNode in goalNodes:
    g.nodes[startNode]['solved'] = True

while not solved(g, startNode):
    gprime = g.subgraph(startNode).copy()
    for i in g.edges:
        if marked(g, i[0], i[1]):
            gprime.add_edge(i[0], i[1])

    n = findleaf(gprime)

    nodeList = list(mainGraph.neighbors(n))

    addToG(n, nodeList)
    s = [n]

    while len(s) != 0:

        for i in s:
            if i not in list(g.neighbors(i)):
                m = s.pop(s.index(i))
                break

        q = {}
        for i in list(g.neighbors(m)):
            if andby(g, m, i):
                q[i] = 2 + costs[i] + costs[andby(g, m, i)]
            else:
                q[i] = 1 + costs[i]

        markList = findMin(q, m)

        for i in markList:
            g.edges[m, i]['marked'] = True
            for j in list(g.neighbors(m)):
                if andby(g, m, j) != i and i != j:
                    g.edges[m, j]['marked'] = False
                    for a in list(g.neighbors(j)):
                        g.edges[j, a]['marked'] = False

        checkNeighbors = True
        for i in g.neighbors(m):
            if marked(g, m, i):
                if not solved(g, i):
                    checkNeighbors = False
        if checkNeighbors:
            g.nodes[m]['solved'] = True

        if costs[m] != q[markList[0]]:
            costs[m] = q[markList[0]]
            for i in list(g.predecessors(m)):
                if marked(g, i, m):
                    s.append(i)

        if solved(g, m):
            for i in list(g.predecessors(m)):
                if marked(g, i, m):
                    s.append(i)

markedge = nx.get_edge_attributes(g, 'marked')
print(markedge)

print("The answer graph contain below edges:")
for i in markedge:
    if markedge[i]:
        print(i)
