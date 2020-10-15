# The class to represent a Node
class Node:
    def __init__(self, value, isAnd, schema):
        self.value = value
        self.isAnd = isAnd
        self.child = []
        # Create graph
        self.schema = schema
        if isAnd:
            self.schema.attr('node', shape='box')
            self.schema.node(self.value)

    def addChild(self, childNode):
        self.child.append(childNode)
        # Add edges for graph
        self.schema.attr('node', shape='circle')
        self.schema.edge(self.value, childNode.value)
