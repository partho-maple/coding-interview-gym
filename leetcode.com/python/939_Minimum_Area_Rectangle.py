class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        minArea = float("inf")
        pointsSet = set()
        for x, y in points:
            pointsSet.add((x, y))
        for x1, y1 in points:
            for x2, y2 in points:
                if (x1, y1) != (x2, y2) and (x1 > x2 and y1 > y2): # To check if the points are not same and if the points are diagonal. Because if the points are diagonal then we will be  able to get both height and width from only this 2 points
                    if (x1, y2) in pointsSet and (x2, y1) in pointsSet: # Check if other 2 points also exists, to form a rectangle
                        area = abs(x1 - x2) * abs(y1 - y2)
                        minArea = min(minArea, area)
        return 0 if minArea == float("inf") else minArea
