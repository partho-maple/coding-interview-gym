

# O(N*Capacity) time |  # O(N*Capacity) space
def knapSackProblem(items, capacity):
    knapSackValues = [[0 for x in range(0, capacity) + 1] for y in range(0, len(items) + 1)]
    for i in range(1, len(items) + 1):
        currentWeight = items[i - 1][1]
        currentValue = items[i - 1][0]
        for individualCapacity in range(0, capacity + 1):
            if currentWeight > capacity:
                knapSackValues[i][individualCapacity] = knapSackValues[i - 1][individualCapacity]
            else:
                knapSackValues[i][individualCapacity] = max(knapSackValues[i - 1][individualCapacity], knapSackValues[i - 1][individualCapacity - currentWeight] + currentValue)
    return [knapSackValues[-1][-1], getKnapsackItems(knapSackValues, items)]


def getKnapsackItems(knapSackValues, items):
    sequence = []
    i = len(knapSackValues) - 1
    individualCapacity = len(knapSackValues[0]) - 1
    while i > 0:
        if knapSackValues[i][individualCapacity] == knapSackValues[i - 1][individualCapacity]:
            i -= 1
        else:
            sequence.append(i - 1)
            individualCapacity -= items[i - 1][1]
            i -= 1
        if individualCapacity == 0:
            break
    return list(reversed(sequence))




