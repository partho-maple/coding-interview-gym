class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanDict = {'I': 1,
                     'V': 5,
                     'X': 10,
                     'L': 50,
                     'C': 100,
                     'D': 500,
                     'M': 1000
                     }
        intNum = 0
        if len(s) == 1:
            return romanDict[s]
        for i in range(len(s) - 1):
            v1 = romanDict[s[i]]
            v2 = romanDict[s[i + 1]]
            if romanDict[s[i]] >= romanDict[s[i + 1]]:
                intNum = romanDict[s[i]] + intNum
            else:
                intNum = intNum - romanDict[s[i]]
        return intNum + romanDict[s[-1]]


sol = Solution()
input = "MCMXCIV"
value = sol.romanToInt(input)
print("Value: ", value)


