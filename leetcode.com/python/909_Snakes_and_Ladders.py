"""
[
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]

[
[4,-1],
[-1,3]]

9, 6
1, 3


6-1-3
"""


class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        rowCount = len(board)
        seen = set()
        queue = collections.deque()
        queue.append((1, 0))  # label, step
        while queue:
            label, step = queue.popleft()
            r, c = self.labelToPosition(label, rowCount)
            if board[r][c] != -1:
                label = board[r][c]
            if label == rowCount * rowCount:  # we have reached to our destination
                return step
            for nextMove in range(1, 7):
                newLabel = label + nextMove
                if newLabel <= rowCount * rowCount and newLabel not in seen:
                    seen.add(newLabel)
                    queue.append((newLabel, step + 1))
        return -1

    def labelToPosition(self, label, rowCount):
        r, c = divmod(label - 1, rowCount)
        if r % 2 == 0:  # even number of row
            return rowCount - 1 - r, c
        else:  # odd number of row
            return rowCount - 1 - r, rowCount - 1 - c
