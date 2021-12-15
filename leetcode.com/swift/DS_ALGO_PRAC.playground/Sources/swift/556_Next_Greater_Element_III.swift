class Solution {
    func nextGreaterElement(_ n: Int) -> Int {
        var nArray = Array(String(n))
        guard nArray.count >= 2 else {
            return -1
        }
        var prevIdx = nArray.count - 1
        for currIdx in stride(from: nArray.count - 2, through: 0, by: -1) {
            prevIdx = currIdx + 1
            if nArray[prevIdx] > nArray[currIdx] {
                var swapIdx = nArray.count - 1
                while swapIdx > currIdx {
                    if nArray[currIdx] < nArray[swapIdx] {
                        nArray.swapAt(swapIdx, currIdx)
                        nArray = Array(nArray[0...currIdx]) + Array(nArray[prevIdx..<nArray.count]).reversed()
                        let result = Int(nArray.map { String($0) }.reduce("") { $0 + $1 })!
                        if result < Int32.max {
                            return result
                        } else {
                            return -1
                        }
                    } else {
                        swapIdx -= 1
                    }
                }
            }
        }
        return -1
    }
}
