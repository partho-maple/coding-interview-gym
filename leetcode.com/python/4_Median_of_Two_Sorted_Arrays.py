
class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        a, b = sorted((nums1, nums2), key=len) # Here we are not sorting the input array. We are sorting the array by length to identity the smallest array to perform search on.
        m, n = len(a), len(b)
        after = (m + n - 1) // 2 # i + j == after, where every number is smaller withi this range a[0:i] + b[0:j] (exclusive)
        # Determine i, j that a[0:i] + b[0:j] (exclusive) is the most small "after" numbers.
        # There could multiple pairs of such (i, j) if there are some duplicated numbers.
        # Each such pair satisfies the following criteria at the same time:
        # 1) i + j == after
        # 2) (j>=1 and a[i] >= b[j-1]) or j==0
        # 3) (i>=1 and b[j] >= a[i-1]) or i==0
        lo, hi = 0, m
        while lo < hi:
            i = (lo + hi) // 2
            j = after - i
            cond1 = (j >= 1 and a[i] >= b[j - 1]) or j == 0
            cond2 = (i >= 1 and b[j] >= a[i - 1]) or i == 0
            if cond1 and cond2:
                lo = i
                break
            elif not cond1:
                # assert (cond2)
                lo = i + 1
            else:
                # assert (cond1)
                hi = i
        i = lo
        j = after - i
        nextfew = sorted(a[i:i + 2] + b[j:j + 2]) # Only sorting 4 elements everytime. so it's O(1)
        return (nextfew[0] + nextfew[1 - (m + n) % 2]) / 2.0







sol = Solution()
num1 = [1, 2]
num2 = [3, 4]
output = sol.findMedianSortedArrays(num1, num2)
print('Res: ', output)