class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        allCandidates = []
        runningCandidate = []
        self.generateCandidates(candidates, runningCandidate, target, allCandidates)
        return allCandidates

    def generateCandidates(self, originalCandidates, runningCandidate, target, allCandidates):
        if sum(runningCandidate) >= target:
            finalCandidate = [candidate for candidate in runningCandidate]
            finalCandidate.sort()
            if sum(runningCandidate) == target and finalCandidate not in allCandidates:
                allCandidates.append(finalCandidate)
            return  # backtrack

        for i in range(len(originalCandidates)):
            choice = originalCandidates[i]
            runningCandidate.append(choice)
            self.generateCandidates(originalCandidates, runningCandidate, target, allCandidates)
            runningCandidate.pop()
