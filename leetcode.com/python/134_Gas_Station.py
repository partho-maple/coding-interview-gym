class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        stationCount = len(gas)
        startingStation = 0
        gasSurplus, gasDeficit = 0, 0
        for i in range(stationCount):
            gasBalance = gas[i] - cost[i] # If we start from i'th station
            if gasBalance + gasSurplus >= 0: # Gas balance for current station + Left over gas from previous station
                gasSurplus += gasBalance    # That means, there is a chance that we can start from this station. So update previous gas balance and move to next station
            else:
                startingStation = i + 1     # We don't have enough gas to move to next station from this station. So we need to start from next station.
                gasDeficit += (gasBalance + gasSurplus)  # Update the gas that we are in short
                gasSurplus = 0
        return startingStation if (gasSurplus + gasDeficit >= 0) else -1    # This is crutil. At the end, if the gas we have left can compenset the gas we are in short, then we can travel all the stations


