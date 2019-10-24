class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxes = [0 for _ in height]  # Initially this will store leftMax values
        leftMax = 0
        for i in range(len(height)):
            maxes[i] = leftMax
            leftMax = max(leftMax, height[i])
        rightMax = 0
        for i in reversed(range(len(height))):
            minHeight = min(maxes[i], rightMax)
            if height[i] < minHeight:
                maxes[i] = minHeight - height[i]
            else:
                maxes[i] = 0
            rightMax = max(rightMax, height[i])
        return sum(maxes)


