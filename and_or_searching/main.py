from and_or_searching.and_or_tree import Node
from and_or_searching.breadth_first_search import BFS
from graphviz import Digraph

# Create graph and edges
schema = Digraph(comment='And/Or Tree', engine='dot')

nodeA = Node('A', False, schema)
nodeB = Node('B', True, schema)
nodeC = Node('C', True, schema)
nodeD = Node('D', False, schema)
nodeE = Node('E', True, schema)
nodeF = Node('F', True, schema)
nodeG = Node('G', False, schema)
nodeH = Node('H', False, schema)
nodeI = Node('I', True, schema)
nodeJ = Node('J', True, schema)
nodeK = Node('K', False, schema)
nodeL = Node('L', True, schema)
nodeM = Node('M', True, schema)
nodeN = Node('N', False, schema)
nodeP = Node('P', False, schema)

nodeE.addChild(nodeI)
nodeE.addChild(nodeJ)
nodeE.addChild(nodeK)

nodeG.addChild(nodeL)
nodeG.addChild(nodeM)

nodeH.addChild(nodeN)
nodeH.addChild(nodeP)

nodeC.addChild(nodeE)
nodeC.addChild(nodeF)

nodeD.addChild(nodeG)
nodeD.addChild(nodeH)

nodeA.addChild(nodeB)
nodeA.addChild(nodeC)
nodeA.addChild(nodeD)

schema.render('tree.gv')

dict_vertex = {'A': nodeA, 'B': nodeB, 'C': nodeC, 'D': nodeD, 'E': nodeE,
               'F': nodeF, 'G': nodeG, 'H': nodeH, 'I': nodeI, 'J': nodeJ,
               'K': nodeK, 'L': nodeL, 'M': nodeM, 'N': nodeN, 'P': nodeP}

start = input("Enter the start node: ")
dest = input("Enter the destination node: ")

# Execute BFS
bfs = BFS(nodeA)

if start not in dict_vertex.keys() or dest not in dict_vertex.keys():
    print("Start Node or Destination Node don't exist!")
else:
    startNode = dict_vertex[start]
    destNode = dict_vertex[dest]
    bfs.execute(startNode, destNode)
