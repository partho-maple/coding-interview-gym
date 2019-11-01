class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ans = 0
        for char in s + t:
            ans ^= char
        return char(ans)




sol = Solution()
out = sol.findTheDifference("abcd", "abcde")
print('Res: ',out)