// Brute-Force. DFS with Backtracking. TLE
class Solution {
    func minPairSum(_ nums: [Int]) -> Int {
        var (minMaxSum, currentSums, usedIndexes) = (Int.max, [Int](), Set<Int>())
        minPairSumDFSHelper(nums, &minMaxSum, &currentSums, &usedIndexes)
        return minMaxSum
    }

    func minPairSumDFSHelper(_ nums: [Int], _ minMaxSum: inout Int, _ currentSums: inout [Int], _ usedIndexes: inout Set<Int>) {
        if usedIndexes.count == nums.count {
            minMaxSum = [currentSums.max()!, minMaxSum].min()!
            return
        }
        for (index, item) in nums.enumerated() {
            if !usedIndexes.contains(index) {
                usedIndexes.insert(index)
                for (index2, item2) in nums.enumerated() {
                    if !usedIndexes.contains(index2) {
                        usedIndexes.insert(index2)
                        let currentSum = item + item2
                        currentSums.append(currentSum)
                        minPairSumDFSHelper(nums, &minMaxSum, &currentSums, &usedIndexes)
                        currentSums.removeLast() // Backtrack
                        usedIndexes.remove(index2) // Backtrack
                    }
                }
                usedIndexes.remove(index) // Backtrack
            }
        }
    }
}

// Greedy with sorting. Accepted. Time: O(nlogn)
class Solution {
    func minPairSum(_ nums: [Int]) -> Int {
        var (minMaxSum, sortedNums, j) = (Int.min, nums.sorted(), nums.count - 1)
        for i in 0..<(sortedNums.count / 2) {
            minMaxSum = [minMaxSum, sortedNums[i] + sortedNums[j]].max()!
            j -= 1
        }
        return minMaxSum
    }
}
