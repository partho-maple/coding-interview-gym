from collections import Counter
def smallestSubstringContaining(bigString, smallString):
    need = Counter(smallString)
	missing = len(smallString)
	left, windowStart, windowEnd = 0, 0, 0
	for right in range(0, len(bigString)):
		currChar = bigString[right]
		if need[currChar] > 0:
			missing -=1
		need[currChar] -= 1
		if missing == 0:
			if windowEnd == 0:
				windowStart, windowEnd = left, right
			while left < right and need[bigString[left]] < 0:
				need[bigString[left]] += 1
				left += 1
				if (right - left) <= (windowEnd - windowStart):
					windowStart, windowEnd = left, right
	return "" if missing > 0 else bigString[windowStart:windowEnd+1]