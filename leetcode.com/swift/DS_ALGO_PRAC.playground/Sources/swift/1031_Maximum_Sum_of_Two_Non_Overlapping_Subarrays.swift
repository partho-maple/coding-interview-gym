class Solution {
    func maxSumTwoNoOverlap(_ A: [Int], _ L: Int, _ M: Int) -> Int {
        var maxSum = 0
        var prefixSumArr = [Int]()
        prefixSumArr.append(0)
        for i in 0..<A.count {
            let curNum = prefixSumArr.last! + A[i]
            prefixSumArr.append(curNum)
        }
        var (startL, endL) = (1, L)
        while endL < prefixSumArr.count {
            let sumL = prefixSumArr[endL] - prefixSumArr[startL - 1]
            var (startM, endM) = (1, M)
            while endM < prefixSumArr.count {
                if startM <= endL && startL <= endM {
                    // Both array overlapping. So M is making a jump through L
                    startM = endL + 1
                    endM = startM + M - 1
                }
                if endM >= prefixSumArr.count {
                    break
                }
                let sumM = prefixSumArr[endM] - prefixSumArr[startM - 1]
                maxSum = max(maxSum, sumL + sumM)
                startM += 1
                endM += 1
            }
            startL += 1
            endL += 1
        }
        return maxSum
    }
}
