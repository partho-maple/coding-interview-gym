class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        triplateCount = 0
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]
                if currentSum < target:
                    triplateCount += (right - left)  # if (i,j,k) works, then (i,j,k), (i,j,k-1),...,(i,j,j+1) all work, totally (k-j) triplets
                    left += 1
                else:
                    while left < right and nums[right] == nums[right - 1]:  # Duplication check
                        right -= 1
                    right -= 1

        return triplateCount


sol = Solution()
# input = [3,1,0,-2]
# target = 4
input = [-2,0,1,3]
target = 2
tripletsNum = sol.threeSumSmaller(input, target)
print("Result: ", tripletsNum)


