from collections import defaultdict
class Solution(object):
    def minSumOfLengths(self, arr, target):
        dp = defaultdict(lambda: float("inf"))
        left, currentWindowSum, result = 0, 0, float("inf")
        for right in range(len(arr)):
            currentWindowSum += arr[right]
            while currentWindowSum > target:
                currentWindowSum -= arr[left]
                left += 1
            if currentWindowSum == target:
                targetArrLen = right - left + 1
                dp[right] = targetArrLen
                result = min(result, dp[left - 1] + dp[right])
            dp[right] = min(dp[right], dp[right - 1])
        return result if result != float("inf") else -1