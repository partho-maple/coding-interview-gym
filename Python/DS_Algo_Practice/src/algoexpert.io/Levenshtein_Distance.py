# https://www.algoexpert.io/questions/Levenshtein%20Distance

# Solution 1
# O(nm) time | O(nm) space
def levenshtein_distance(str1, str2):
    # Here, rows count is 'len(str2) + 1' and column count is 'len(str1) + 1'
    # And first row initialises like [0, 1, 2, 3, 4, ...]
    edits = [[x for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    for i in range(1, len(str2) + 1):
        edits[i][0] = edits[i - 1][0] + 1
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[i - 1]:
                edits[i][j] = edits[i - 1][j - 1]
            else:
                edits[i][i] = 1 + min(edits[i -1][j - 1], edits[i - 1][j], edits[i][j - 1])
    return edits[-1][-1] # this return the final value (last cell) of 2D array


