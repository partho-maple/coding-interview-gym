# Approach 1: Brute force solution. Time Limit exceeded
class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        cache = {}
        self.checkRecordHelper(n, "", cache, ["A", "L", "P"])
        return sum(cache.values())

    def checkRecordHelper(self, totalCount, currentRecord, cache, attendenceChars):
        if len(currentRecord) > totalCount:
            return
        for char in attendenceChars:
            currentRecord += char
            if len(currentRecord) == totalCount:
                cache[currentRecord] = self.checkReward(currentRecord)
            self.checkRecordHelper(totalCount, currentRecord, cache, attendenceChars)
            currentRecord = currentRecord[:-1]  # Backtrack

    def checkReward(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        absentCount = 0
        lateCount = 0
        for char in s:
            if char == 'A':
                absentCount += 1
                lateCount = 0
            elif char == 'L':
                lateCount += 1
            else:
                lateCount = 0
            if absentCount > 1 or lateCount > 2:
                return False
        return True

# Approach 2: Brute force solution. Pruning state state space tree. Time Limit exceeded. 17 / 58 test cases passed.
class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        cache = {}
        self.totalReward = 0
        self.checkRecordHelper(n, "", cache, ["A", "L", "P"])
        return self.totalReward

    def checkRecordHelper(self, totalCount, currentRecord, cache, attendenceChars):
        if currentRecord and currentRecord in cache and cache[currentRecord] is False:
            return
        if len(currentRecord) >= totalCount:
            return
        for char in attendenceChars:
            currentRecord += char
            cache[currentRecord] = self.checkReward(currentRecord)
            if len(currentRecord) == totalCount and cache[currentRecord] == True:
                self.totalReward += 1
            self.checkRecordHelper(totalCount, currentRecord, cache, attendenceChars)
            currentRecord = currentRecord[:-1]  # Backtrack

    def checkReward(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        absentCount = 0
        lateCount = 0
        for char in s:
            if char == 'A':
                absentCount += 1
                lateCount = 0
            elif char == 'L':
                lateCount += 1
            else:
                lateCount = 0
            if absentCount > 1 or lateCount > 2:
                return False
        return True


# Approach 3: DP
class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 3
        if n == 0:
            return 0
        mod = 1000000007
        dp = [0 for i in range(n + 1)]
        dp[0], dp[1], dp[2] = 1, 2, 4
        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % mod
        res = dp[n]

        # inserting A into (n-1)-length strings
        for i in range(1, n + 1):
            res += ((dp[i - 1] * dp[n - i]) % mod)
        res = res % mod
        return res
