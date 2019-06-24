

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        leftIndex = 0
        rightIndex = len(s) - 1
        while leftIndex  < rightIndex:
            if s[leftIndex].isalnum() is False:
                leftIndex += 1
                continue
            if s[rightIndex].isalnum() is False:
                rightIndex -= 1
                continue
            if s[leftIndex] != s[rightIndex]:
                return False
            leftIndex += 1
            rightIndex -= 1
        return True


obj = Solution()
isPalin = obj.isPalindrome("A man, a plan, a canal: Panama")
print("Result: ", isPalin)

