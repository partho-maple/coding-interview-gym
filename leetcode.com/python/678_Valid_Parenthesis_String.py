# Source: https://tinyurl.com/yad2akx6
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cmin, cmax = 0, 0  # openCount in range [cmin, cmax]
        for ch in s:
            if ch == "(":
                cmin += 1
                cmax += 1
            elif ch == ")":
                cmin -= 1
                cmax -= 1
            elif ch == "*":
                cmax += 1  # if `*` become `(` then openCount++
                cmin -= 1  # if `*` become `)` then openCount--
                # if `*` become `` then nothing happens
                # So openCount will be in new range [cmin-1, cmax+1]
            if cmax < 0:
                return False  # Don't have enough openCount -> Invalid
            cmin = max(cmin, 0)  # Keep openCount >= 0
        return cmin == 0  # Return true if can found `openCount == 0` in range [cmin, cmax]
