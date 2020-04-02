class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = 0
        for i in range(N + 1):
            numStr = str(i)
            if ("3" in numStr) or ("4" in numStr) or ("7" in numStr):
                continue
            numStrRotated = ""
            for digit in numStr:
                if digit == "0":
                    numStrRotated = numStrRotated + "0"
                elif digit == "1":
                    numStrRotated = numStrRotated + "1"
                elif digit == "2":
                    numStrRotated = numStrRotated + "5"
                elif digit == "5":
                    numStrRotated = numStrRotated + "2"
                elif digit == "6":
                    numStrRotated = numStrRotated + "9"
                elif digit == "8":
                    numStrRotated = numStrRotated + "8"
                elif digit == "9":
                    numStrRotated = numStrRotated + "6"

            if numStr != numStrRotated:
                count += 1
        return count