# Approach 1: Prefix sum + Sliding Window
# Time: O(Cols x  min(Rows, Cols) x Rows)
class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        rows, cols = len(mat), len(mat[0])
        maxSideLegth = 0
        for left in range(cols):
            prefixRowSumForCol = [0 for i in range(rows)]
            right = left
            while right < min(rows, cols):
                for i in range(rows):
                    prefixRowSumForCol[i] += mat[i][right]
                currentSideLength = right - left + 1
                isSquareSumValid = self.isSquareSumValid(prefixRowSumForCol, currentSideLength, threshold)
                if isSquareSumValid:
                    maxSideLegth = max(maxSideLegth, currentSideLength)
                right += 1
        return maxSideLegth

    def isSquareSumValid(self, nums, windowSize, threshold):
        left, right = 0, 0
        currentSum = 0
        for i in range(windowSize):  # advance right to fill the window initially
            currentSum += nums[i]
            right = i
            if right == windowSize:
                break
        while right < len(nums) - 1:
            currentSum -= nums[left]
            left += 1
            right += 1
            currentSum += nums[right]
            if currentSum <= threshold:
                return True
        return currentSum <= threshold




# Approach 1: Prefix sum + Binary Search. Prefix sum for a col is sorted. sso we can perform BS
# Time: O(Cols x  min(Rows, Cols) x log Rows)
class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        rows, cols = len(mat), len(mat[0])
        maxSideLegth = 0
        for left in range(cols):
            prefixRowSumForCol = [0 for i in range(rows)]
            prefixColSum = [0 for i in range(rows + 1)]
            right = left
            while right < min(rows, cols):
                for i in range(rows):
                    prefixRowSumForCol[i] += mat[i][right]
                prefixColSum = list(prefixRowSumForCol)
                for i in range(1, rows):
                    prefixColSum[i] += prefixColSum[i - 1]
                currentSideLength = right - left + 1
                isSquareSumValid = self.isSquareSumValid(prefixColSum, currentSideLength, threshold)
                # print("isSquareSumValid: ", isSquareSumValid)
                if isSquareSumValid:
                    maxSideLegth = max(maxSideLegth, currentSideLength)
                right += 1
        return maxSideLegth

    def isSquareSumValid(self, nums, windowSize, threshold):
        left, right = 0, len(nums)
        currentMidSum = 0
        while left < right:
            mid = left + (right - left)//2
            # print("-------")
            # print("mid: ", mid)
            # print("nums: ", nums)
            # print("windowSize: ", windowSize)
            currentMidSum = nums[mid]
            if currentMidSum <= threshold:
                if mid <= windowSize:
                    return True
                else:
                    left = mid + 1
            else:
                right = mid
        return currentMidSum <= threshold

