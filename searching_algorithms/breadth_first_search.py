# The class to represent a Node
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None


# The class to represent the Breath First Search algorithm
class BFS:
    def __init__(self, graph):
        self.graph = graph
        self.queue = []       # Queue for BFS
        self.tree = {}        # Tree for BFS

    # Execute the Breath First Search algorithm
    def execute(self, start, dest, dict_vertex):
        # List for vertices visited
        visited = []

        # Create BFS tree
        self.tree[start] = Node(start)

        # Mark the source node as visited and enqueue it
        self.queue.append(start)
        visited.append(start)

        while self.queue:
            # Dequeue a vertex from queue and print it
            s = self.queue.pop(0)

            # Get all adjacent vertices of the dequeue vertex s.
            # If a adjacent has not been visited, then mark it visited and enqueue it
            for i in self.graph[s]:
                if i not in visited:
                    self.queue.append(i)
                    visited.append(i)
                    # Add adjacent to Tree BFS
                    self.tree[i] = Node(i)
                    self.tree[i].parent = self.tree[s]

        # Show the path to destination
        if dest not in self.tree.keys():
            print("Don't have the path to " + dict_vertex[dest])
        else:
            path = [dest]
            node = self.tree[dest]
            while node.parent:
                node = node.parent
                path.append(node.value)

            print('The path is: ', end="")
            for i in path[::-1]:
                if i == dest:
                    print(dict_vertex[i], end="")
                else:
                    print(dict_vertex[i] + ' -> ', end="")
