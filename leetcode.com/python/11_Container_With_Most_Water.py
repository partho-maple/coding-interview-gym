class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        maxWaterArea = 0
        while left < right:
            minHeight = min(height[left], height[right])
            maxWaterArea = max(maxWaterArea, minHeight * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxWaterArea
