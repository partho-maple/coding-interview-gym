from collections import deque


# Source:   https://tinyurl.com/vd3dtch
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        if k == 0:
            return nums
        deq = deque()
        result = []
        for idx in range(k):
            while deq:
                if nums[idx] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break
            deq.append(idx)
        for idx in range(k, len(nums)):
            result.append(nums[deq[0]])
            if deq[0] < idx - k + 1:
                deq.popleft()
            while deq:
                if nums[idx] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break
            deq.append(idx)
        result.append(nums[deq[0]])
        return result

