# My initial brute force solution. Off-course I got TLE. Man, I am so so stupid.
# Only 10 / 85 test cases passed.
class Solution(object):
    def maximumMinimumPath(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        allMinPathValues = []
        currentPath = [A[0][0]]
        visiitedSet = set()
        visiitedSet.add((0, 0))
        self.maximumMinimumPathDFSHelper(A, allMinPathValues, currentPath, 0, 0, visiitedSet)
        print("allMinPathValues: ", allMinPathValues)
        return max(allMinPathValues)

    def maximumMinimumPathDFSHelper(self, A, allMinPathValues, currentPath, r, c, visiitedSet):
        if r >= len(A) - 1 and c >= len(A[0]) - 1:
            print("currentPath: ", currentPath)
            allMinPathValues.append(min(list(currentPath)))
            return
        neighbours = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for neighbour in neighbours:
            dr, dc = neighbour[0], neighbour[1]
            newR, newC = r + dr, c + dc
            if 0 <= newR < len(A) and 0 <= newC < len(A[0]):
                if (newR, newC) not in visiitedSet:
                    visiitedSet.add((newR, newC))
                    currentPath.append(A[newR][newC])
                    self.maximumMinimumPathDFSHelper(A, allMinPathValues, currentPath, newR, newC, visiitedSet)
                    currentPath.pop()
                    visiitedSet.discard((newR, newC))

import heapq
class Solution(object):
    def maximumMinimumPath(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        visiitedSet = set()
        visiitedSet.add((0, 0))
        rowCount, colCount = len(A), len(A[0])
        maxMin = float("inf")
        maxHeap = [(-A[0][0], 0, 0)]
        while maxHeap:
            val, r, c = heapq.heappop(maxHeap)
            originalVal = -val
            maxMin = min(originalVal, maxMin)
            if r == rowCount - 1 and c == colCount - 1:
                return maxMin

            neighbours = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for neighbour in neighbours:
                dr, dc = neighbour[0], neighbour[1]
                newR, newC = r + dr, c + dc
                if 0 <= newR < len(A) and 0 <= newC < len(A[0]) and ((newR, newC) not in visiitedSet):
                    visiitedSet.add((newR, newC))
                    heapq.heappush(maxHeap, (-A[newR][newC], newR, newC))
        return maxMin



"""
the scode of this path 8 →  4 →  5 →  9 is 4 
(because 4 is the minimum elemet/value of this path)
And that's why it's the score of this path

Annd we need to find the max value of ssuch paths

so find the maximum of minimum value in a path

[5,4,5],
[1,2,6],
[7,4,6]

 0123
0''''
1'
2'
3'










('currentPath: ', [2, 2, 1, 2, 2, 2, 2])
('currentPath: ', [2, 2, 1, 2, 2, 1, 2])
('currentPath: ', [2, 2, 1, 2, 2, 1, 2, 2, 2])
('currentPath: ', [2, 2, 1, 2, 2, 2, 2, 2, 2])
('currentPath: ', [2, 2, 1, 2, 2, 2, 2, 1, 2])
('currentPath: ', [2, 2, 2, 2, 1, 2, 2, 2, 2])
('currentPath: ', [2, 2, 2, 2, 1, 2, 2, 1, 2])
('currentPath: ', [2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2])
('currentPath: ', [2, 2, 2, 2, 2, 2, 2, 2, 2])
('currentPath: ', [2, 2, 2, 2, 2, 2, 2, 1, 2])
('currentPath: ', [2, 2, 2, 2, 2, 1, 2, 2, 2])
('currentPath: ', [2, 2, 2, 2, 2, 1, 2])
('currentPath: ', [2, 1, 2, 2, 1, 2, 2, 2, 2])
('currentPath: ', [2, 1, 2, 2, 1, 2, 2, 1, 2])
('currentPath: ', [2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2])
('currentPath: ', [2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2])
('currentPath: ', [2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2])
('currentPath: ', [2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2])
('currentPath: ', [2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2])
('currentPath: ', [2, 1, 2, 2, 2, 2, 2, 2, 2])
('currentPath: ', [2, 1, 2, 2, 2, 2, 2, 1, 2])
('currentPath: ', [2, 1, 2, 2, 2, 1, 2, 2, 2])
('currentPath: ', [2, 1, 2, 2, 2, 1, 2])
('allMinPathValues: ', [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

"""