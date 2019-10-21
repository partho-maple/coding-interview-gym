import sys



# Top-Down approach. But solution has Excedd the Time Limit
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount < 1:
            return 0
        numOfCoins = [float('inf') for n in range(amount + 1)]
        numOfCoins[0] = 0
        return self.coinChangeHelper(coins, amount, numOfCoins)


    def coinChangeHelper(self, coins, remainder, numOfCoins):
        # minimum coins to make change for negative amount is -1.
        # this is just a base case we arbitrary define
        if remainder < 0:
            return -1
        # the minimum number of coins to make change for 0 is always 0
        if remainder == 0:
            return 0
        # If we already have the answer cached, just return it
        if numOfCoins[remainder] != float('inf'):
            return numOfCoins[remainder]
        # No answer yet. Try each coin as the last coin in the change that we make for the amount
        for coin in coins:
            changeResultForRestAmount = self.coinChangeHelper(coins, remainder - coin, numOfCoins)
            if changeResultForRestAmount >= 0:
                numOfCoins[remainder] = min(numOfCoins[remainder], changeResultForRestAmount + 1)
        return numOfCoins[remainder] if numOfCoins[remainder] != float('inf') else -1




# Top-Down approach (Recursive). But solution has been accepted
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount < 1:
            return 0
        numOfCoins = [float('inf') for n in range(amount + 1)]
        numOfCoins[0] = 0
        return self.coinChangeHelper(coins, amount, numOfCoins)


    def coinChangeHelper(self, coins, remainder, numOfCoins):
        # minimum coins to make change for negative amount is -1.
        # this is just a base case we arbitrary define
        if remainder < 0:
            return -1
        # the minimum number of coins to make change for 0 is always 0
        if remainder == 0:
            return 0
        # If we already have the answer cached, just return it
        if numOfCoins[remainder] != float('inf'):
            return numOfCoins[remainder]
        # No answer yet. Try each coin as the last coin in the change that we make for the amount
        minimum = sys.maxint
        for coin in coins:
            changeResultForRestAmount = self.coinChangeHelper(coins, remainder - coin, numOfCoins)
            if changeResultForRestAmount >= 0 and changeResultForRestAmount < minimum:
                minimum = changeResultForRestAmount + 1
        numOfCoins[remainder] = -1 if minimum == sys.maxint else minimum
        return numOfCoins[remainder]




# Bottom-Up approach (Iterative). But solution has been accepted
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount < 1:
            return 0
        numOfCoins = [float('inf') for n in range(amount + 1)]
        numOfCoins[0] = 0
        for coin in coins:
            for n in range(amount + 1):
                if coin <= n:
                    numOfCoins[n] = min(numOfCoins[n], numOfCoins[n - coin] + 1)
        return numOfCoins[amount] if numOfCoins[amount] != float('inf') else -1






sol = Solution()
minCoin = sol.coinChange([2], 3)
print("Minimum number of coin: ", minCoin)


