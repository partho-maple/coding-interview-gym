from collections import deque

# My original code - GOT TLE
class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        origin, destination = (0, 0), (abs(x), abs(y))
        currentLevel = 0
        if origin == destination:
            return currentLevel
        queue = deque([(origin, currentLevel)])
        visitedSet = set()
        visitedSet.add(origin)
        while queue:
            currentPosition, currentLevel = queue.popleft()
            currentPossileMoves = self.getPossileMoves(currentPosition[0], currentPosition[1])
            for move in currentPossileMoves:
                if move not in visitedSet and move[0] > -4 and move[1] > -4:
                    if currentPosition == destination:
                        return currentLevel
                    visitedSet.add(move)
                    queue.append((move, currentLevel + 1))
        return currentLevel

    def getPossileMoves(self, x, y):
        moves = [(x + 2, y + 1), (x + 2, y - 1), (x - 2, y + 1), (x - 2, y - 1), (x + 1, y + 2), (x - 1, y + 2), (x + 1, y - 2), (x - 1, y - 2)]
        return moves





# Source: https://tinyurl.com/wed5c6s  Same as mine but  - GOT Accepted
from collections import deque
class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if (x, y)==(0, 0):return 0
        def bfs(i, j, x, y):
            open_list = deque([(i,j,0)])
            seen = {(i, j)}
            while open_list:
                i, j, d = open_list.popleft()
                for di, dj in [(1,2),(2,1),(1,-2),(2,-1),
                               (-1,2),(-2,1), (-1,-2),(-2,-1)]:
                    r, c = i+di, j+dj
                    if (r,c) not in seen and r>-4 and c>-4:
                        if (r,c)==(x,y):return d+1
                        seen.add((r,c))
                        open_list.append((r,c,d+1))
        return bfs(0,0,abs(x), abs(y))