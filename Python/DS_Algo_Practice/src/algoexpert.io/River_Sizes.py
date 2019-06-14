# https://www.algoexpert.io/questions/River%20Sizes


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



