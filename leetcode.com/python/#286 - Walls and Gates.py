class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        gateDistanceGrid = [['-inf' for value in row] for row in rooms]
        for i in rooms:
            for j in rooms[j]:
                if gateDistanceGrid[i][j] is not '-inf':
                    continue
                else:
                    gateDistanceGrid[i][j] = 'INF'
                    gateDistance = self.traverseNode(i, j, rooms, gateDistanceGrid)
                    if gateDistance > 0:
                        gateDistanceGrid[i][j] = gateDistance
        return gateDistanceGrid



    def traverseNode(self, i, j, rooms, gateDistanceGrid):
        gateDistance = 0
        nodesToExplore = [[i, j]] # This is a queue, because we are performing BFS
        while nodesToExplore:
            currentNode = nodesToExplore.pop(0)
            i = currentNode[0]
            j = currentNode[1]
            if rooms[i][j] == -1:
                continue
            if rooms[i][j] == 0:
                gateDistance += 1
                gateDistanceGrid[i][j] = gateDistance
                break
            unvisitedNeighbour = self.getUnvisitedNeighbour(i, j, rooms, gateDistanceGrid)
            for neighbour in unvisitedNeighbour:
                nodesToExplore.append(neighbour)
        return gateDistance



    def getUnvisitedNeighbour(self, i, j, rooms, gateDistanceGrid):
        unvisitedNeighbours = []
        if i > 0:
            unvisitedNeighbours.append([i - 1, j])
        if i < len(rooms) - 1:
            unvisitedNeighbours.append([i + 1, j])
        if j > 0:
            unvisitedNeighbours.append([i, j - 1])
        if j < len(rooms[0]) - 1:
            unvisitedNeighbours.append([i, j + 1])
        return unvisitedNeighbours




# Driver Code
sol = Solution()
gateDistanceGrid = sol.wallsAndGates()








