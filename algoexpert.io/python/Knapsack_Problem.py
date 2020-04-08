# 0/1 knapsack
# O(N*Capacity) time |  # O(N*Capacity) space
# My solution, Passes
def knapsackProblem(items, capacity):
    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(items))]

    # Populate the first row for first item
    for cap in range(capacity + 1):
        val, wei = items[0]  # first item
        if cap >= wei:
            dp[0][cap] = val

    for itemIdx in range(1, len(items)):
        for cap in range(1, capacity + 1):
            val, wei = items[itemIdx]
            cValue1, cValue2 = 0, 0
            if wei <= cap:
                cValue1 = val + dp[itemIdx - 1][cap - wei]
            cValue2 = dp[itemIdx - 1][cap]
            dp[itemIdx][cap] = max(cValue1, cValue2)
    return [dp[-1][-1], buildItemSequence(dp, items, capacity)]


def buildItemSequence(dp, items, capacity):
    sequence = []
    currentItemIdx, currentCapacity = len(items) - 1, capacity
    while currentItemIdx >= 0:
        if dp[currentItemIdx][currentCapacity] == dp[currentItemIdx - 1][currentCapacity]:
            currentItemIdx -= 1
        else:
            sequence.append(currentItemIdx)
            currentCapacity -= items[currentItemIdx][1]
            currentItemIdx -= 1
        if currentCapacity == 0:
            break
    return list(reversed(sequence))


# Provided solution by Algoexpert
def knapsackProblem(items, capacity):
    knapsackValues = [[0 for x in range(0, capacity + 1)] for y in range(0, len(items) + 1)]
    for i in range(1, len(items) + 1):
        currentWeight = items[i - 1][1]
        currentValue = items[i - 1][0]
        for c in range(0, capacity + 1):
            if currentWeight > c:
                knapsackValues[i][c] = knapsackValues[i - 1][c]
            else:
                knapsackValues[i][c] = max(knapsackValues[i - 1][c], knapsackValues[i - 1][c - currentWeight] + currentValue)
    return [knapsackValues[-1][-1], getKnapsackItems(knapsackValues, items)]

def getKnapsackItems(knapsackValues, items):
    sequence = []
    i = len(knapsackValues) - 1
    c = len(knapsackValues[0]) - 1
    while i > 0:
        if knapsackValues[i][c] == knapsackValues[i - 1][c]:
            i -= 1
        else:
            sequence.append(i - 1)
            c -= items[i - 1][1]
            i -= 1
        if c == 0:
            break
    return list(reversed(sequence))



