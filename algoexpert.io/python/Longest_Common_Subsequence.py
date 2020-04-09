# Solution:  My solution using 2d dp
# O(nm) time | O(nm) space
def longestCommonSubsequence(string1, string2):
    dp = [[[] for _ in range(len(string2) + 1)] for _ in range(len(string1) + 1)]
	for i in range(1, len(string1) + 1):
		x = string1[i - 1]
		for j in range(1, len(string2) + 1):
			rx = string2[j - 1]
			if x == rx:
				dp[i][j] = dp[i - 1][j - 1] + [x]
			else:
				dp[i][j] = max(dp[i][j - 1], dp[i - 1][j], key=len)
	return dp[-1][-1]


