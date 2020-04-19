class Solution(object):
    def dfs(self, start, end, record):
        if start >= end:
            return 0

        if start + 1 == end:
            return start

        if record[start][end] is None:
            pays = []
            for i in range(start, end + 1):
                prevPay = self.dfs(start, i - 1, record)
                nextPay = self.dfs(i + 1, end, record)
                currPay = i
                totlPay = currPay + max(prevPay, nextPay)
                pays.append(totlPay)

            record[start][end] = min(pays)

        return record[start][end]

    def getMoneyAmount(self, n):
        record = [[None] * (n + 1) for _ in range(n + 1)]
        return self.dfs(1, n, record)