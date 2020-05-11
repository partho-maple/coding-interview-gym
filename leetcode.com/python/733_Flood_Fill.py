from collections import deque
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        queue = deque([(sr, sc)])
        startingColor = image[sr][sc]
        image[sr][sc] = newColor
        while queue:
            currentLevelSize = len(queue)
            while currentLevelSize > 0:
                currentLevelSize -= 1
                sourceR, sourceC = queue.popleft()
                neighbours = [(-1,0),(0,1),(1,0),(0,-1)]
                for neighbour in neighbours:
                    dr, dc = neighbour
                    newSR, newSC = sourceR + dr, sourceC + dc
                    if 0 <= newSR < len(image) and 0 <= newSC < len(image[0])  and image[newSR][newSC] == startingColor and image[newSR][newSC] != newColor:
                        queue.append((newSR, newSC))
                        image[newSR][newSC] = newColor
        return image