# https://leetcode.com/problems/binary-search/


class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid
            elif nums[mid] > target:
                r = mid
            else:
                return mid
        return -1




# Your MyLinkedList object will be instantiated and called as such:
obj = Solution()

index = obj.search([2], 2)
print("Index: ", index)