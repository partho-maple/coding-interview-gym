# My initial solution. 14 / 30 test cases passed.
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        zeros = []
        for i in range(len(arr)):
            if arr[i] == 0:
                zeros.append(i)
        for i in zeros:
            if i + 2 < len(arr):
                prevNum = arr[i + 1]
                arr[i + 1] = 0
                for j in range(i + 2, len(arr)):
                    currrentNum = arr[j]
                    arr[j] = prevNum
                    prevNum = currrentNum

# Vary inefficient solution. Does't respect the constraints.
class Solution:
	def duplicateZeros(self, arr):
		i = 0
		n = len(arr)
		while(i<n):
			if arr[i] == 0:
				arr.pop()
				arr.insert(i,0)
				i+=1
			i+=1

# Optimised and good solution
# Source: https://tinyurl.com/qnxv356
class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        shift = 0
        l = len(arr)
        for i in range(l):
            if arr[i] == 0:
                shift += 1
        for i in range(l-1, -1, -1):
            # put the shifted number in the right spot
            if i + shift < l:
                arr[i+shift] = arr[i]
            # if we meet a 0, we need to duplicate 0
            if arr[i] == 0:
                shift -= 1
                if i + shift < l:
                    arr[i+shift] = 0