class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            is_forward = nums[i] >= 0  # if we are moving forward or not
            slow, fast = i, i

            # if slow or fast becomes '-1' this means we can't find cycle for this number
            while True:
                # move one step for slow pointer
                slow = self.find_next_index(nums, is_forward, slow)
                # move one step for fast pointer
                fast = self.find_next_index(nums, is_forward, fast)
                if (fast != -1):
                    # move another step for fast pointer
                    fast = self.find_next_index(nums, is_forward, fast)
                if slow == -1 or fast == -1 or slow == fast:
                    break

            if slow != -1 and slow == fast:
                return True

        return False

    def find_next_index(self, arr, is_forward, current_index):
        direction = arr[current_index] >= 0

        if is_forward != direction:
            return -1  # change in direction, return -1

        next_index = (current_index + arr[current_index]) % len(arr)

        # one element cycle, return -1
        if next_index == current_index:
            next_index = -1

        return next_index



sol = Solution()
nums = [-1,-2,-3,-4,-5]
out = sol.circularArrayLoop(nums)
print("Res: ", out)