from collections import defaultdict


class Graph:
    """
    Create graph for condition statements
    Ex: A -> B
    """

    def __init__(self):
        self.graph = defaultdict(list)

    def add_condition_statement(self, arg1, arg2):
        self.graph[arg1].append(arg2)

    def print_graph(self):
        for k, v in self.graph.items():
            print(k)
            for i in v:
                print(' |-> ' + i)
            print('\n')

    def get_graph(self):
        return self.graph


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None


def law_of_syllogism(graph, start, dest):
    """
    Law of syllogism

    1. P -> Q
    2. Q -> R
    3. Therefore: P -> R

    Using Breath First Search algorithm to perform Law of syllogism
    """

    queue = []
    tree = {}

    # Flag to check have path from start to dest
    flag = None

    # List for vertices visited
    visited = []

    # Create BFS tree
    tree[start] = Node(start)

    # Mark the start node as visited and enqueue it
    queue.append(start)
    visited.append(start)

    while queue:
        # Dequeue a vertex from queue
        s = queue.pop(0)

        # Get all adjacent vertices of the dequeue vertex s.
        # If a adjacent has not been visited, then mark it visited and enqueue it
        for i in graph[s]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
                # Add adjacent to Tree BFS
                tree[i] = Node(i)
                tree[i].parent = tree[s]

    # Check the path to destination
    if dest not in tree.keys():
        flag = False
    else:
        flag = True

    return flag


def modus_ponens(graph, arg1, arg2, antecedent_list):
    """
    Modus ponens

    1. arg1 -> arg2 (First premise is a conditional statement)
    2. arg1 (Second premise is the antecedent)
    3. arg2 (Conclusion deduced is the consequent)
    """

    # String for first and second premise
    premise = '1. ' + arg1 + ' -> ' + arg2 + '\n' + '2. ' + arg1 + '\n' + '-' * 20 + '\n' + '3. '

    if not law_of_syllogism(graph, arg1, arg2):
        return "Don't exist the conclusion"
    else:
        if arg1 not in antecedent_list:
            return "Don't exist the conclusion"
        else:
            return premise + arg2


def modus_tollens(graph, arg1, arg2, negative_consequent_list):
    """
    Modus tollens

    1. arg1 -> arg2 (First premise is a conditional statement)
    2. ¬arg2 (Second premise is the negation of the consequent)
    3. ¬arg1 (Conclusion deduced is the negation of the antecedent)
    """

    # String for first and second premise
    premise = '1. ' + arg1 + ' -> ' + arg2 + '\n' + '2. ¬' + arg2 + '\n' + '-' * 20 + '\n' + '3. '

    if not law_of_syllogism(graph, arg1, arg2):
        return "Don't exist the conclusion"
    else:
        if arg2 not in negative_consequent_list:
            return "Don't exist the conclusion"
        else:
            return premise + '¬' + arg1


if __name__ == '__main__':
    # Create first premise
    g = Graph()
    g.add_condition_statement('P', 'Q')
    g.add_condition_statement('Q', 'R')
    # g.print_graph()

    # Create list of antecedent
    ant_list = ['P', 'Q']

    # Create list of the negation of the consequent
    cons_list = ['Q', 'R']

    # Deduction Reasoning
    conclusion1 = modus_ponens(g.get_graph(), 'P', 'R', ant_list)
    print(conclusion1)

    print('\n\n')

    conclusion2 = modus_ponens(g.get_graph(), 'P', 'K', ant_list)
    print(conclusion2)

    print('\n\n')

    conclusion3 = modus_tollens(g.get_graph(), 'P', 'Q', cons_list)
    print(conclusion3)

    print('\n\n')

    conclusion4 = modus_tollens(g.get_graph(), 'P', 'A', cons_list)
    print(conclusion4)
