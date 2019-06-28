# https://leetcode.com/problems/binary-search/


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) <= 0:
            return -1
        nums.sort()
        return self.searchHealper(nums, target, 0, len(nums) - 1)

    def searchHealper(self, nums, target, startIndex, endIndex):
        while endIndex >= 0:
            if startIndex == endIndex and nums[startIndex] != target:
                break
            if startIndex == endIndex and nums[startIndex] == target:
                return startIndex
            mid = (endIndex - startIndex) // 2 + startIndex
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                endIndex = mid - 1
            else:
                startIndex = mid + 1
        return -1




# Your MyLinkedList object will be instantiated and called as such:
obj = Solution()

index = obj.search([2], 2)
print("Index: ", index)