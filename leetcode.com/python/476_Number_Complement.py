class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bitCount, numCopy = 0, num
        while numCopy > 0:
            bitCount += 1
            numCopy = numCopy >> 1

        allBitsSet = pow(2, bitCount) - 1
        return num ^ allBitsSet
