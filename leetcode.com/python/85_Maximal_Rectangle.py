
#   Solution 1: Using Histograms - Stack
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        heights = [0 for _ in matrix[0]]
        maxRect = float('-inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == "0":
                    heights[j] = 0
                else:
                    heights[j] += 1
            maxRect = max(maxRect, self.largestRectangleArea(heights))
        return maxRect


    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [-1]
        finalArea = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                finalArea = max(finalArea, height *width)
            stack.append(i)
        heights.pop()
        return finalArea





sol = Solution()
input = [["1","0"]]
output = sol.maximalRectangle(input)
print('Res: ', output)