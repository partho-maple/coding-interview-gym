
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/discuss/346505/Binary-classification-Python.-Detailed-explanation-Turtle-Code
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/discuss/256765/Python-Binary-search-with-detailed-explanation

class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        low, high = max(weights), sum(weights)
        while low < high:
            # Guess the capacity of the ship
            mid = (low + high) // 2

            current_capacity = 0 # loaded capacity of current ship
            numberOfShip = 1 # number of ship needed

            #----simulating loading the weight to ship one by one----#
            for weight in weights:
                current_capacity += weight
                if current_capacity > mid:  # current ship meets the capacity
                    current_capacity = weight
                    numberOfShip += 1
            # ---------------simulation ends--------------------------#

            # we need too many ships, so we need to increase capacity to reduce num of ships needed
            if numberOfShip > D:
                low = mid + 1
            # we are able to ship with good num of ships, but we still need to find the optimal max capacity
            else:
                high = mid

        return low





sol = Solution()
input1 = [3,2,2,4,1,4]
input2 = 3
output = sol.shipWithinDays(input1, input2)
print('Res: ', output)


