// Brute force DFS. Wrong anserr for some cases
class Solution {
    func longestSubsequence(_ arr: [Int], _ difference: Int) -> Int {
        guard arr.count > 1 else {
            return 1
        }
        var maxLength = 1
        for i in 0..<arr.count {
            longestSubsequenceDFSHelper(arr, difference, i, 1, &maxLength)
        }
        return maxLength
    }

    func longestSubsequenceDFSHelper(_ arr: [Int], _ difference: Int, _ currentStartIndex: Int, _ currentLength: Int, _ maxLength: inout Int) {
        if currentStartIndex >= arr.count - 1 {
            maxLength = [maxLength, currentLength].max()!
        }
        for i in currentStartIndex..<arr.count {
            let currentDiff = arr[i] - arr[currentStartIndex]
            if currentDiff == difference {
                longestSubsequenceDFSHelper(arr, difference, i, currentLength + 1, &maxLength)
            }
        }
    }
}

// DP, Accepted. Time O(n)
class Solution {
    func longestSubsequence(_ arr: [Int], _ difference: Int) -> Int {
        guard arr.count > 1 else {
            return 1
        }
        var (maxLength, dp) = (1, [Int:Int]()) // arr itemas key and length till i as value
        dp[arr.first!, default: 0] += 1
        for i in 1..<arr.count {
            let pre = arr[i] - difference
            dp[arr[i], default: 0] = 1 + (dp[pre] ?? 0)
            maxLength = [maxLength, dp[arr[i]]!].max()!
        }
        return maxLength
    }
}
