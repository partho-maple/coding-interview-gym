class Solution(object):

    # Greedy Approach. BFS to be precise.
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps, currentEnd, currentFarthest = 0, 0, 0
        for i in range(len(nums) - 1):
            currentFarthest = max(currentFarthest, i + nums[i])
            if i == currentEnd:
                jumps += 1
                currentEnd = currentFarthest
        return jumps




sol = Solution()
input = [2,3,1,1,4]
output = sol.jump(input)
print("Res: ", output)