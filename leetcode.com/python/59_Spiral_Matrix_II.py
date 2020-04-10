class Solution(object):
    def generateMatrix(self, n):
        values = [i for i in range(1, n * n + 1)]
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        sR, eR, sC, eC = 0, n - 1, 0, n - 1

        valueIdx = 0
        while sR <= eR and sC <= eC:
            for i in range(sC, eC + 1):
                matrix[sR][i] = values[valueIdx]
                valueIdx += 1

            for i in range(sR + 1, eR + 1):
                matrix[i][eC] = values[valueIdx]
                valueIdx += 1

            for i in range(eC - 1, sC - 1, -1):
                if sR == eR:
                    break
                matrix[eR][i] = values[valueIdx]
                valueIdx += 1

            for i in range(eR - 1, sR, -1):
                if sC == eC:
                    break
                matrix[i][sC] = values[valueIdx]
                valueIdx += 1

            sR += 1
            eR -= 1
            sC += 1
            eC -= 1

        return matrix
