import bisect


# 1.    Since array is sorted, find index of the value closest to x (using binary search)
# 2.    Expand left and right by k elements
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        idx = bisect.bisect(arr, x)  # using binary search to determind the position index of x into arr. Here, idx is the immediate right index of x
        leftIdx, rightIdx = idx - 1, idx  # initially leftIdx is the index of x
        result = []
        while len(result) != k:
            leftNum = arr[leftIdx] if leftIdx >= 0 else float("inf")
            rightNum = arr[rightIdx] if rightIdx < len(arr) else float("inf")
            if abs(x - leftNum) - abs(x - rightNum) <= 0:
                result.append(leftNum)
                leftIdx -= 1
            else:
                result.append(rightNum)
                rightIdx += 1
        return sorted(result)  # this sorting is O(1) operation




sol = Solution()
arr = [1,2,3,4,5]
k=4
x=3
output = sol.findClosestElements(arr,k,x)
print("Res: ", output)