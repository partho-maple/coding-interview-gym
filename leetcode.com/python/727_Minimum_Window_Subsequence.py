# Two Pointer/ Sliding Window approach: https://tinyurl.com/vs9qedt
# O(1) space and O(mn) complexity.
class Solution(object):
    def minWindow(self, S, T):
        """
we can conduct two steps by using two pointers for this problem:
     1. check feasibility from left to right
     2. check optimization from right to left
we can traverse from left to right, find a possible candidate until reach the first ending character of T
eg: for the string s = abcdebdde and t = bde, we should traverse s string until we find first e,
i.e. abcde, then traverse back from current "e" to find if we have other combination of bde with smaller length.

@param right: fast pointer that always points the last character of T in S
@param left: slow pointer that used to traverse back when right pointer find the last character of T in S
@param tIndex: third pointer used to scan string T
@param minLen: current minimum length of subsequence
        """
        if not S or not T:
            return ""
        right, minLength = 0, float("inf")
        result = ""

        while right < len(S):
            tIndex = 0
            while right < len(S):                                   #   Use fast pointer to find  the last char of T in S
                if S[right] == T[tIndex]:
                    tIndex += 1
                if tIndex == len(T):
                    break
                right += 1

            if right == len(S):                                     #   If right pointer is over than boundery
                break

            # Use another slow pointer to traverse from right to left to find the first character of T in S
            left = right
            tIndex = len(T) - 1
            while left >= 0:
                if S[left] == T[tIndex]:
                    tIndex -= 1
                if tIndex < 0:
                    break
                left -= 1

            if (right - left + 1) < minLength:                      #   If we found another optimal subsequence then update the result
                minLength = right - left + 1
                result = S[left:right + 1]

            right = left + 1                                        #   We have to move right pointer to the next position of the left pointer, not the next position of right pointer

        return result




sol = Solution()
S = "abcdebdde"
T = "bde"
out = sol.minWindow(S, T)
print("Res: ",out)