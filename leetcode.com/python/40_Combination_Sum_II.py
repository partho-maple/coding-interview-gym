class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        allCandidates ,runningCandidate = [], []
        self.generateCandidates(candidates, target, 0, runningCandidate, allCandidates)
        return allCandidates

    def generateCandidates(self, originalCandidates, target, startingIndex, runningCandidate, allCandidates):
        if sum(runningCandidate) >= target:
            finalCandidate = sorted(list(runningCandidate))
            if sum(finalCandidate) == target and finalCandidate not in allCandidates:
                allCandidates.append(finalCandidate)
            return

        for i in range(startingIndex, len(originalCandidates)):
            candidate = originalCandidates[i]
            runningCandidate.append(candidate)
            self.generateCandidates(originalCandidates, target, i + 1, runningCandidate, allCandidates)
            runningCandidate.pop() # Backtracking
