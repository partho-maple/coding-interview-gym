def isMonotonic(array):
    if len(array) <= 2:
        return True
    for i in range(1, len(array) - 1):
        prevN = array[i - 1]
        currN = array[i]
        nextN = array[i + 1]
        if prevN <= currN <= nextN or prevN >= currN >= nextN:
            continue
        else:
            return False
    return True

