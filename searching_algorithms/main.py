from searching_algorithms.graph_adjacency_list import Graph
from searching_algorithms.breadth_first_search import BFS

dict_vertex = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i'}

# Create graph and edges
graph = Graph()

graph.add_edge(0, 4)
graph.add_edge(0, 6)
graph.add_edge(1, 0)
graph.add_edge(3, 2)
graph.add_edge(4, 0)
graph.add_edge(4, 5)
graph.add_edge(6, 0)
graph.add_edge(6, 4)
graph.add_edge(6, 7)
graph.add_edge(7, 8)
graph.add_edge(8, 7)
graph.add_edge(8, 2)

graph.print_graph(dict_vertex)

# Execute BFS
bfs = BFS(graph.get_graph())

start = input("Enter the start node: ")
dest = input("Enter the destination node: ")

if start not in dict_vertex.values() or dest not in dict_vertex.values():
    print("Start Node or Destination Node don't exist!")
else:
    startNode = list(dict_vertex.keys())[list(dict_vertex.values()).index(start)]
    destNode = list(dict_vertex.keys())[list(dict_vertex.values()).index(dest)]
    bfs.execute(startNode, destNode, dict_vertex)
