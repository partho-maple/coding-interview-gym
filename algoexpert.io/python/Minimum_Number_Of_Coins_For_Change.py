# O(nd) time | O(n) space
# Where, 'n' is amount and 'd' is number of denominators
# Provideo solution by algoexpert
def minNumberOfCoinsForChange(n, denoms):
    num_of_coins = [float("inf") for amount in range(n + 1)]
    num_of_coins[0] = 0
    for denom in denoms:
        for amount in range(len(num_of_coins)):
            if denom <= amount:
                num_of_coins[amount] = min(num_of_coins[amount], num_of_coins[amount - denom] + 1)
    return num_of_coins[n] if num_of_coins[n] != float("inf") else -1


# My solution
def minNumberOfCoinsForChange(n, denoms):
    dp = [[float("inf") for _ in range(n + 1)] for _ in range(len(denoms))]
    denoms = sorted(denoms)
    print("-----")
    print(denoms)
    # Populate first row
    for amount in range(1, n + 1):
        if amount >= denoms[0]:
            count = int(amount // denoms[0])
            dp[0][amount] = count

    for i in range(len(denoms)):
        dp[i][0] = 0

    for denomIdx in range(1, len(denoms)):
        for amount in range(1, n + 1):
            denom = denoms[denomIdx]
            choich1, choice2 = float("inf"), float("inf")
            if amount >= denom and dp[denomIdx][amount - denom] != float("inf"):
                choich1 = 1 + dp[denomIdx][amount - denom]
            choice2 = dp[denomIdx - 1][amount]
            dp[denomIdx][amount] = min(choich1, choice2)
    print(dp)
    return dp[-1][-1]


