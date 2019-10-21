

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        threeLargest = [None, None, None]
        for num in nums:
            self.updateThreelargest(threeLargest, num)
        if threeLargest[0] is None:
            return threeLargest[2]
        else:
            return threeLargest[0]



    def updateThreelargest(self, threeLargest, num):
        if threeLargest[2] is None or num > threeLargest[2]:
            self.shiftAndUpdateLargest(threeLargest, num, 2)
        elif threeLargest[1] is None or num > threeLargest[1]:
            self.shiftAndUpdateLargest(threeLargest, num, 1)
        elif threeLargest[0] is None or num > threeLargest[0]:
            self.shiftAndUpdateLargest(threeLargest, num, 0)



    def shiftAndUpdateLargest(self, threeLargest, num, index):
        if num in threeLargest:
            return
        # Since the index/range is exclusive in python, so we need to add 1 here. For example, if we put range(2), then the value will be 0 to 1, exlcuding last range. So we need to add 1 here to include the last index into the range.
        for i in range(index + 1):
            if i == index:
                threeLargest[index] = num

            else:
                threeLargest[i] = threeLargest[i + 1]




obj = Solution()

index = obj.thirdMax([2, 2, 3, 1])
print("Max: ", index)