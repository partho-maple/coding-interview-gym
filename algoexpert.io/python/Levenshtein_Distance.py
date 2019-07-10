# https://www.algoexpert.io/questions/Levenshtein%20Distance

# Solution 1
# O(nm) time | O(nm) space
def levenshtein_distance(str1, str2):
    # Here, rows count is 'len(str2) + 1' and column count is 'len(str1) + 1'
    edits = [[x for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    # And first column initialises like [0, 1, 2, 3, 4, ...]
    for i in range(1, len(str2) + 1):
        edits[i][0] = edits[i - 1][0] + 1
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[i - 1]:
                edits[i][j] = edits[i - 1][j - 1]
            else:
                edits[i][i] = 1 + min(edits[i -1][j - 1], edits[i - 1][j], edits[i][j - 1])
    return edits[-1][-1] # this return the final value (last cell) of 2D array


# Solution 2
# O(nm) time | O (min(n, m)) space
def levenshtein_distance(str1, str2):
    small = str1 if len(str1) < len(str2) else str2 # this would be the column count
    big = str1 if len(str1) >= len(str2) else str2  # this would be the row count
    even_edits = [x for x in range(len(small) + 1)] # This essentially means the even rows
    odd_edits = [None for x in range(len(small) + 1)]  # This essentially means the odd rows
    for i in range(1, len(big) + 1):
        if i % 2 == 1:
            current_edits = odd_edits
            previous_edits = even_edits
        else:
            current_edits = even_edits
            previous_edits = odd_edits
        current_edits[0] = i
        for j in range(1, len(big) + 1):
            if big[i - 1] == small[j - 1]:
                current_edits[j] = previous_edits[j - 1]
            else:
                current_edits[j] = 1 + min(previous_edits[j - 1], previous_edits[j], current_edits[j - 1])
    return even_edits[-1] if len(big) % 2 == 0 else odd_edits[-1]





