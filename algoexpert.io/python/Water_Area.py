

# Time O(n) | Space O(n)
def waterArea(heights):
    maxes = [0 for x in heights]
    leftMax = 0
    for i in range(len(heights)):
        height = heights[i]
        maxes[i] = leftMax
        leftMax = max(leftMax, height)
    rightMax = 0
    for i in reversed(range(len(heights))):
        height = heights[i]
        minHeight = min(rightMax, maxes[i])
        if height < minHeight:
            maxes[i] = minHeight - height
        else:
            maxes[i] = 0
        rightMax = max(rightMax, height)
    return sum(maxes)


def waterArea(heights):
    leftMaxHeights = [0 for _ in heights]
    currentLeftMax = 0
    for i in range(len(heights)):
        height = heights[i]
        leftMaxHeights[i] = currentLeftMax
        currentLeftMax = max(currentLeftMax, height)

    rightMaxHeights = [0 for _ in heights]
    currentRightMax = 0
    for i in reversed(range(len(heights))):
        height = heights[i]
        rightMaxHeights[i] = currentRightMax
        currentRightMax = max(currentRightMax, height)

    maxes = [0 for _ in heights]
    for i in range(len(heights)):
        minHeight = min(leftMaxHeights[i], rightMaxHeights[i])
        if minHeight > heights[i]:
            maxes[i] = minHeight - heights[i]
    return sum(maxes)