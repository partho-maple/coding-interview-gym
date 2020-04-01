# Approach 0: Brute force. My initial solution
# Time: O(n * K)
# 61 / 61 test cases passed, but took too long.
class Solution(object):
    def kEmptySlots(self, bulbs, K):
        """
        :type bulbs: List[int]
        :type K: int
        :rtype: int
        """
        minDay = -1
        positions = [0 for _ in range(len(bulbs))]
        for i in range(len(bulbs)):
            position = bulbs[i] - 1
            day = i + 1
            positions[position] = 1
            left, right = position - K - 1, position + K + 1
            if left >= 0:
                isValid = True
                for j in range(left, position):
                    if (j == left):
                        if positions[j] == 0:
                            isValid = False
                            break
                    else:
                        if positions[j] == 0:
                            continue
                        elif positions[j] == 1:
                            isValid = False
                            break
                if isValid:
                    minDay = day
                    break
            if right < len(bulbs):
                isValid = True
                for j in range(position + 1, right + 1):
                    if (j == right):
                        if positions[j] == 0:
                            isValid = False
                            break
                    else:
                        if positions[j] == 0:
                            continue
                        elif positions[j] == 1:
                            isValid = False
                            break
                if isValid:
                    minDay = day
                    break
        return minDay



# Approach 1: Sliding window
# O(n)
# Source: https://tinyurl.com/qsenvnd
class Solution(object):
    def kEmptySlots(self, bulbs, K):
        """
        :type bulbs: List[int]
        :type K: int
        :rtype: int
        """
        L = len(bulbs)
        onDaysToTurnOn = [0] * L
        for day, bulbPosToTurnOn in enumerate(bulbs):
            onDaysToTurnOn[bulbPosToTurnOn - 1] = day

        answer = -1
        left = 0
        right = left + K + 1
        for bulbPosToTurnOn, dayToTurnOn in enumerate(onDaysToTurnOn):
            if right >= L:
                break
            earliestDay = max(onDaysToTurnOn[left], onDaysToTurnOn[right])
            if dayToTurnOn > earliestDay:
                continue
            if bulbPosToTurnOn == right:
                if earliestDay < answer or answer == -1:
                    answer = earliestDay + 1
            left = bulbPosToTurnOn
            right = left + K + 1
        return answer



