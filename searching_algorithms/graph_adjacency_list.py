from collections import defaultdict


# A class to represent a graph. A graph is the list of the adjacency lists.
# Size of the array will be the no. of the vertices "V"
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # Add edges
    def add_edge(self, startVertex, nextVertex):
        self.graph[startVertex].append(nextVertex)

    # Print the graph
    def print_graph(self, dict_vertex):
        for k, v in self.graph.items():
            print(dict_vertex[k])
            for i in v:
                print('-> ' + dict_vertex[i])
            print('\n')

    # Return the graph
    def get_graph(self):
        return self.graph
