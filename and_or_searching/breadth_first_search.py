# The class to represent a Node
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None


# The class to represent the Breath First Search algorithm
class BFS:
    def __init__(self, root):
        self.root = root
        self.queue = []  # Queue for BFS
        self.tree = {}  # Tree for BFS

    # Execute the Breath First Search algorithm
    def execute(self, startNode, destNode):
        # List for vertices visited
        visited = []

        # Create BFS tree
        self.tree[str(startNode.value)] = Node(str(startNode.value))

        # Mark the source node as visited and enqueue it
        self.queue.append(startNode)
        visited.append(startNode.value)

        while self.queue:
            # Dequeue a vertex from queue and print it
            s = self.queue.pop(0)

            # Get all adjacent vertices of the dequeue vertex s.
            # If a adjacent has not been visited, then mark it visited and enqueue it
            listAnd = str()
            listOr = []
            for i in s.child:
                if i.value not in visited:
                    self.queue.append(i)
                    visited.append(i.value)
                    # Add adjacent to Tree BFS
                    if i.isAnd:
                        listAnd += str(i.value)
                    else:
                        listOr.append(str(i.value))

            # Add adjacent to Tree BFS
            index = None
            for k in self.tree.keys():
                if str(s.value) in k:
                    index = str(k)
                    break

            if index:
                if listAnd != '':
                    self.tree[listAnd] = Node(listAnd)
                    self.tree[listAnd].parent = self.tree[index]
                for k in listOr:
                    self.tree[k] = Node(k)
                    self.tree[k].parent = self.tree[index]
            else:
                if listAnd != '':
                    self.tree[listAnd] = Node(listAnd)
                    self.tree[listAnd].parent = self.tree[str(s.value)]
                for k in listOr:
                    self.tree[k] = Node(k)
                    self.tree[k].parent = self.tree[str(s.value)]

        # Show the path to destination
        index = None
        for k in self.tree.keys():
            if destNode.value in k:
                index = k
                break

        if not index:
            print("Don't have the path to " + destNode.value)
        else:
            path = [destNode.value]
            node = self.tree[index]
            while node.parent:
                node = node.parent
                path.append(node.value)

            print('The path is: ', end="")
            for i in path[::-1]:
                if i == destNode.value:
                    print(i, end="")
                else:
                    print(i + ' -> ', end="")
