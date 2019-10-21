class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count=0
        for c in S:
            if c in J:
                count += 1
        return count