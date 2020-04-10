def spiralTraverse(matrix):
    result = []
    sR, eR, sC, eC = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    while sR <= eR and sC <= eC:
        for i in range(sC, eC + 1):
            result.append(matrix[sR][i])

        for i in range(sR + 1, eR + 1):
            result.append(matrix[i][eC])

        for i in range(eC - 1, sC - 1, -1):
            if sR == eR:
                break
            result.append(matrix[eR][i])

        for i in range(eR - 1, sR, -1):
            if sC == eC:
                break
            result.append(matrix[i][sC])

        sR += 1
        eR -= 1
        sC += 1
        eC -= 1

    return result
