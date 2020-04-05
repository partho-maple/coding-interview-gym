# https://www.algoexpert.io/questions/Breadth-first%20Search
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self] # step 1 > add root node to the queue, the node on which we are calling BFS
        while len(queue) > 0:
            current = queue.pop(0) # step 2 > pop the root/current node
            array.append(current.name) # step 3 > add the current node to the final array
            for child in current.children: # step 4 > add the children of the current node to the queue
                queue.append(child)
        return array


