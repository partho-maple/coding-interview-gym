import collections
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        sCounter = Counter(S)
        j = set(J)
        jwels = 0
        for stone in sCounter:
            if stone in j:
                jwels += sCounter[stone]
        return jwels