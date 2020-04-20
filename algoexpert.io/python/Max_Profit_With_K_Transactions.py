#   Solution 1
#   O(nk) time | O(nk) space
def maxProfitWithKTransaction(prices, k):
    if not len(prices):
        return 0
    profits = [[0 for day in prices] for transaction in range(len(k + 1))]
    for transaction in range(1, k + 1):
        maxThusFar = float('-inf')
        for day in range(1, prices + 1):
            maxThusFar = max(maxThusFar, profits[transaction - 1][day - 1] - prices[day - 1])
            profits[transaction][day] = max(profits[transaction][day - 1], maxThusFar + prices[day])
    return profits[-1][-1]


#   Solution 2
#   O(nk) time | O(n) space
def maxProfitWithKTransaction(prices, k):
    if not len(prices):
        return 0
    evenProfits = [0 for d in prices]
    oddProfits = [0 for d in prices]
    for transaction in range(1, k + 1):
        maxThusFar = float('-inf')
        if transaction % 2 == 1:
            currentProfits = oddProfits
            previousProfits = evenProfits
        else:
            currentProfits = evenProfits
            previousProfits = oddProfits
        for day in range(1, prices + 1):
            maxThusFar = max(maxThusFar, previousProfits[day - 1] - prices[day - 1])
            currentProfits[day] = max(currentProfits[day - 1], maxThusFar + prices[day])
    return evenProfits[-1] if k % 2 == 0 else oddProfits[-1]





