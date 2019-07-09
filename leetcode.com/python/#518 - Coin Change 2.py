class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        ways = [0 for n in range(amount + 1)]
        ways[0] = 1
        for coin in coins:
            for checkingAmount in range(1, amount + 1):
                if coin <= checkingAmount:
                    ways[checkingAmount] += ways[checkingAmount - coin]
        return ways[-1]
