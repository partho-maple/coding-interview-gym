# Source:   https://tinyurl.com/tdhj9eh
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # 1)    Taking XOR of all numbers in the given array will give us XOR of num1 and num2,
        #       calling this XOR as n1xn2.
        n1xn2 = 0
        for num in nums:
            n1xn2 ^= num

        # 2)    Get the rightmost bit that is '1'.
        #       Find any bit which is set in n1xn2.
        #       We can take the rightmost bit which is ‘1’. Let’s call this rightmostSetBit
        rightMostSetBit = 1
        while (rightMostSetBit & n1xn2) == 0:
            rightMostSetBit = rightMostSetBit << 1
        num1, num2 = 0, 0

        for num in nums:
            if (num & rightMostSetBit) != 0:  # the bit is set
                num1 ^= num
            else:
                num2 ^= num                     # the bit is not set

        return [num1, num2]