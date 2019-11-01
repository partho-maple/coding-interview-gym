
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seenOnce, seenTwice = 0, 0
        for num in nums:
            # first appearance:
            # add num to seen_once
            # don't add to seen_twice because of presence in seen_once

            # second appearance:
            # remove num from seen_once
            # add num to seen_twice

            # third appearance:
            # don't add to seen_once because of presence in seen_twice
            # remove num from seen_twice
            seenOnce = ~seenTwice & (seenOnce ^ num)
            seenTwice = ~seenOnce & (seenTwice ^ num)
        return seenOnce




sol = Solution()
input = [2,2,3,2]
output = sol.singleNumber(input)
print('Res: ', output)





