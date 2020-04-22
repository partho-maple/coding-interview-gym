def longestPeak(array):
    longestPeakLen = 0
    i = 1
    while i < len(array) - 1:
        isPeak = array[i - 1] < array[i] > array[i + 1]
        if not isPeak:
            i += 1
            continue

        leftIdx = i - 2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx -= 1

        rightIdx = i + 2
        while rightIdx < len(array) and array[rightIdx - 1] > array[rightIdx]:
            rightIdx += 1

        currentPeakLen = rightIdx - leftIdx - 1
        longestPeakLen = max(longestPeakLen, currentPeakLen)
        i = rightIdx

    return longestPeakLen

