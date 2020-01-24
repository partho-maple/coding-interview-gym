from collections import deque
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        level, queue, visited = -1, deque(['0000']), set(deadends)
        while queue:
            level += 1
            currentLevelSize = len(queue)
            for _ in range(currentLevelSize):
                currentNode = queue.popleft()
                if currentNode == target:
                    return level
                if currentNode in visited:
                    continue
                visited.add(currentNode)
                currentNodesNeighour = self.nodeNeighbours(currentNode)
                queue.extend(currentNodesNeighour)
        return -1



    def nodeNeighbours(self, sourceNode):
        neighbours = []
        for i, char in enumerate(sourceNode):
            num = int(char)
            neighbours.append(sourceNode[:i] + str((num + 1) % 10) + sourceNode[i + 1:])
            neighbours.append(sourceNode[:i] + str((num - 1) % 10) + sourceNode[i + 1:])
        return neighbours

