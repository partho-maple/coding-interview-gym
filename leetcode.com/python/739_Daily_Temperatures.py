class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        result = [0 for _ in range(len(T))]
        stack = []
        for i in range(len(T) - 1, -1, -1):
            while stack:
                temperature, day = stack[-1]
                if T[i] >= temperature:
                    stack.pop()
                else:
                    break
            if stack:
                temperature, day = stack[-1]
                result[i] = day - i
            stack.append((T[i], i))
        return result