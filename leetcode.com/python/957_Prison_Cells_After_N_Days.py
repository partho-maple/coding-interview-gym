"""
{
'[0, 1, 0, 0, 0, 1, 0, 0]': 1000000001, ----
'[0, 1, 0, 1, 0, 0, 1, 0]': 999999992,
'[0, 0, 1, 1, 1, 0, 0, 0]': 15,
'[0, 1, 0, 0, 1, 1, 1, 0]': 1000000000,
'[0, 0, 0, 1, 1, 1, 0, 0]': 999999997,
'[0, 1, 0, 0, 1, 0, 1, 0]': 999999999,
'[0, 0, 1, 0, 1, 0, 1, 0]': 999999995,
'[0, 1, 0, 1, 0, 1, 0, 0]': 13,
'[0, 1, 1, 1, 0, 0, 1, 0]': 999999993,
'[0, 0, 1, 0, 0, 0, 1, 0]': 999999994,
'[0, 1, 0, 0, 1, 0, 0, 0]': 999999998,
'[0, 0, 1, 1, 1, 1, 1, 0]': 999999996, ------
'[0, 1, 1, 1, 1, 1, 0, 0]': 14,
'[0, 0, 0, 1, 0, 0, 1, 0]': 999999991}

"""
# My initial code. 248 / 258 test cases passed.
# Forward calculations
class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        seen = {}
        lastSeenCells = []
        currentDay = 0
        while currentDay < N:
            cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
            key = str(cells)
            if key in seen:
                div, mod = divmod(N, currentDay)
                currentDay = N - mod
            currentDay += 1
            seen[key] = currentDay
            lastSeenCells = cells
        print(seen)
        return lastSeenCells

    def prisonAfterNDays(self, cells, N):
        seen = {str(cells): N}
        while N:
            seen.setdefault(str(cells), N)
            N -= 1
            cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
            if str(cells) in seen:
                N %= seen[str(cells)] - N
        return cells


# https://tinyurl.com/yczdwnwu
# Backword calculations
class Solution(object):
    def prisonAfterNDays(self, cells, N):
        seen = {str(cells): N}
        while N:
            seen.setdefault(str(cells), N)
            N -= 1
            cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
            if str(cells) in seen:
                N %= seen[str(cells)] - N
        return cells