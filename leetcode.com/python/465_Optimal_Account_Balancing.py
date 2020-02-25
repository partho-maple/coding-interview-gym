from collections import defaultdict

class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        balance = defaultdict(int)
        for transaction in transactions:
            X, Y, Z = transaction[0], transaction[1], transaction[2]
            balance[X] -= Z
            balance[Y] += Z

        debts = balance.values()
        minTransactions = self.dfs(0, debts)
        return minTransactions

    def dfs(self, currentPersonIdx, debts):
        while currentPersonIdx < len(debts) and debts[currentPersonIdx] == 0:
            currentPersonIdx += 1
        if currentPersonIdx == len(debts):
            return 0

        minTransaction = float("inf")
        for i in range(currentPersonIdx + 1, len(debts)):
            if debts[currentPersonIdx] * debts[i] < 0:
                # settle currentPersonIdx debt with i'th person's debt
                debts[i] += debts[currentPersonIdx]
                minTransaction = min(minTransaction, 1 + self.dfs(currentPersonIdx + 1, debts))
                # backtrack and try with next possible value to settle currentPersonIdx debt, to find out the min transsactions
                debts[i] -= debts[currentPersonIdx]
        return minTransaction