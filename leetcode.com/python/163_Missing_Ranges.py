class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        nums.insert(0, lower - 1)
        nums.append(upper + 1)
        res = []
        i = 0
        while i < len(nums) - 1:
            leftRage, rightRange = nums[i], nums[i + 1]
            if leftRage != (rightRange - 1):
                if rightRange - leftRage == 2:
                    res.append(str(rightRange - 1))
                elif rightRange - leftRage > 2:
                    res.append("{}->{}".format(leftRage + 1, rightRange - 1))
            i += 1
        return res