# Solution #1
#   O(n^2) time | O(n) space
def minNumberOfJumps(array):
	aLen = len(array)
	if aLen == 1:
		return 0
    dp = [float("inf") for _ in range(aLen)]
	dp[0] = 0
	for destiinationIdx in range(1, aLen):
		for sourceIdx in range(0, destiinationIdx):
			if sourceIdx + array[sourceIdx] >= destiinationIdx:
				dp[destiinationIdx] = min(dp[destiinationIdx], dp[sourceIdx] + 1)
	return dp[-1]

# Solution #2
# O(n) time | O(1) space
def minNumberOfJumps(array):
    if len(array) == 1:
        return 0
    jumps = 0
    maxReach = array[0]
    steps = array[0]
    for i in range(1, len(array) - 1):
        maxReach = max(maxReach, i + array[i])
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = maxReach - 1
    return jumps + 1