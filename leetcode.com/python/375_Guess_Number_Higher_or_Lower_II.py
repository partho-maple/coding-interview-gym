class Solution(object):
    def dfs(self, start, end, record):
        if start >= end:
            return 0

        if start + 1 == end:
            return start

        if record[start][end] is None:
            record[start][end] = min(
                (i + max(self.dfs(start, i - 1, record), self.dfs(i + 1, end, record))) for i in range(start, end + 1)
            )

        return record[start][end]

    def getMoneyAmount(self, n):
        record = [[None] * (n + 1) for _ in range(n + 1)]
        return self.dfs(1, n, record)