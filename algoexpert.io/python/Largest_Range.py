

# O(n) time | O(n) space
def largestRange(array):
    bestRange = []
    longestLength = 0
    nums = {}
    for num in array:
        nums[num] = True
    for num in array:
        if not nums[num]:
            continue
        nums[num] = False
        currentLenght = 1
        left = num - 1
        right = num + 1
        while left in nums:
            nums[left] = False
            currentLenght += 1
            left -= 1
        while right in nums:
            nums[right] = False
            currentLenght += 1
            right += 1
        if currentLenght > longestLength:
            longestLength = currentLenght
            bestRange = [left + 1, right - 1]
    return bestRange
