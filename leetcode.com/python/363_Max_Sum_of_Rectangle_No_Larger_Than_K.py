import bisect
class Solution(object):

    def maxSubArraylessK(self, nums, k):
        """
        we need to find the sum[right]-sum[left]<=k
        since the bitsect return the index of the sorted value
        we can't directly pop the nums[idx]
        we should use insort from the bisect
        """
        # python set() doesn't support indexing, using list instead
        # similar as the c++ or java set()

        prefixSum = [] # It will keep the sums in sorted order.
        prefixSum.append(0)
        maxSumSoFar = float("-inf")
        currentRightBound = 0
        for rightIdx in range(len(nums)):
            currentRightBound += nums[rightIdx]
            # find the lower/left bound/sum of the index
            possibleLeftBound = currentRightBound - k  # since (possibleLeftBound + K =  currentRightBound)
            possibleLeftBoundInsertionIndex = bisect.bisect_left(prefixSum, possibleLeftBound)
            # find max in prefixSum[right] - prefixSum[left] <= k
            if 0 <= possibleLeftBoundInsertionIndex < len(prefixSum):
                maxSumSoFar = max(maxSumSoFar, currentRightBound - prefixSum[possibleLeftBoundInsertionIndex])  # this (currentRightBound - prefixSum[possibleLeftBoundInsertionIndex]) ensures that we are taking the sum that just smaller than K
            # using insort instead of append since bisect_left reason
            bisect.insort(prefixSum, currentRightBound) # To keep the prefixSum sorted
        return maxSumSoFar

    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        """
        The python solution hasn't a good time performance,
        since lack some of the datatype to do 
        I am trying to imitate the way solved in c++ or Java
        Ther related quesiton might be:
        1. #53. Maximum Subarray 
        2. Maximum Subarray sum less or equal than K
        3. maximun sum of rectangle 
        """
        if not matrix or not matrix[0]:
            return 0
        row, col = len(matrix), len(matrix[0])
        result = float("-inf")
        # using two pointer to record the scan position
        for left in range(col):
            # reset mem to store the row data
            currentSums = [0 for _ in range(row)]
            # since the rectange has area>0
            right = left
            while right < col:
                # count one row
                for i in range(row):
                    currentSums[i] += matrix[i][right]
                # find the max in this row
                currentSumsMax = self.maxSubArraylessK(currentSums, k)
                result = max(result, currentSumsMax)
                right += 1
        return result



[[1,0,1],[0,-2,3]]
2

[[2,1,-3,-4,5],[0,6,3,4,1],[2,-2-1,4,-5],[-3,3,1,0,3]]
[[6,-5,-7,4,-4]]