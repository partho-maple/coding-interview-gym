class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = ''.join(S.split('-')).upper()
        reminder = K if len(S) % K == 0 else len(S) % K
        currentIdx = reminder
        resultS = S[:currentIdx]
        while currentIdx < len(S):
            resultS += '-' + S[currentIdx: currentIdx + K]
            currentIdx += K
        return resultS



sol = Solution()
input = "5F3Z-2e-9-w"
output = sol.licenseKeyFormatting(input, 4)
print('Output: ', output)