# https://www.algoexpert.io/questions/River%20Sizes

# Approach 1: Using BFS
# O(wh) time | O(wh) space
def river_size(matrix):
    size = []  # It would contain all of our river sizes
    visited = [[False for value in row] for row in matrix] # auxiliary matrix to store wather a node is visited or not
    for i in range(len(matrix)): # iterate through rows of the matrix
        for j in range(len(matrix[i])): # iterate through each entry/column of the row
            if visited[i][j]: # if the entry is visited then just skip
                continue
            traverse_node(i, j, matrix, visited, size) # is not visited then process
    return size


def traverse_node(i, j, matrix, visited, size): # This is using DFS, iteration
    current_river_size = 0
    nodes_to_explore = [[i, j]] # A stack to store th nodes
    while len(nodes_to_explore):
        current_node = nodes_to_explore.pop()
        i = current_node[0]
        j = current_node[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        current_river_size += 1
        unvisited_neighbour = get_unvisited_neighbours(i, j, matrix, visited)
        for neighbour in unvisited_neighbour:
            nodes_to_explore.append(neighbour)
    if current_river_size > 0:
        size.append(current_river_size)


def get_unvisited_neighbours(i, j, matrix, visited):
    unvisited_neighbours = []
    if i > 0 and not visited[i - 1][j]:
        unvisited_neighbours.append([i - 1][j])
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisited_neighbours.append([i + 1][j])
    if j > 0 and not visited[i][j - 1]:
        unvisited_neighbours.append([i][j - 1])
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisited_neighbours.append([i][j + 1])
    return unvisited_neighbours



# Approach 2: Using Disjoin Sets
class DJS(object):
    def __init__(self, numOfElements):
        self.n = numOfElements
        self.parents = [0 for _ in range(numOfElements)]
        self.rank = [0 for _ in range(numOfElements)]
        self.makeSet()

    def makeSet(self):
        for i in range(self.n):
            self.parents[i] = i

    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)
        if parentX == parentY:
            return
        if self.rank[parentX] > self.rank[parentY]:
            self.parents[parentY] = parentX
        elif self.rank[parentX] < self.rank[parentY]:
            self.parents[parentX] = parentY
        else:
            self.parents[parentX] = parentY
            self.rank[parentY] += 1

    def find(self, x):
        parentX = self.parents[x]
        if x != parentX:
            parentX = self.find(parentX)
        return parentX


from collections import defaultdict
def riverSizes(matrix):
    if not matrix:
        return []
    rowCount, colCount = len(matrix), len(matrix[0])
    djs = DJS(rowCount * colCount)
    for i in range(rowCount):
        for j in range(colCount):
            val = matrix[i][j]
            if val == 0:
                continue

    if i + 1 < rowCount and matrix[i + 1][j] == 1:
        djs.union(i * (colCount) + j, (i + 1) * (colCount) + j)

    if i - 1 >= 0 and matrix[i - 1][j] == 1:
        djs.union(i * (colCount) + j, (i - 1) * (colCount) + j)

    if j + 1 < colCount and matrix[i][j + 1] == 1:
        djs.union(i * (colCount) + j, (i) * (colCount) + j + 1)

    if j - 1 >= 0 and matrix[i][j - 1] == 1:
        djs.union(i * (colCount) + j, (i) * (colCount) + j - 1)

    ilands = defaultdict(int)
    for i in range(rowCount):
        for j in range(colCount):
            if matrix[i][j] == 1:
                val = i * colCount + j
                parent = djs.find(val)
                ilands[parent] += 1

    return ilands.values()
