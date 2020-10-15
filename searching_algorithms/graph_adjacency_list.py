from collections import defaultdict
from graphviz import Digraph


# A class to represent a graph. A graph is the list of the adjacency lists.
# Size of the array will be the no. of the vertices "V"
class Graph:
    def __init__(self, dict_vertex):
        self.graph = defaultdict(list)
        self.dict_vertex = dict_vertex
        self.schema = Digraph(comment='BFS', engine='sfdp')
        self.schema.attr('node', shape='circle', size='8.5')

    # Add edges
    def add_edge(self, startVertex, nextVertex):
        self.graph[startVertex].append(nextVertex)
        self.schema.edge(self.dict_vertex[startVertex], self.dict_vertex[nextVertex])

    # Print the graph
    def print_graph(self):
        for k, v in self.graph.items():
            print(self.dict_vertex[k])
            for i in v:
                print('-> ' + self.dict_vertex[i])
            print('\n')

    # Return the graph
    def get_graph(self):
        return self.graph

    # Return the schema
    def get_schema(self):
        return self.schema.render('bfs.gv')
