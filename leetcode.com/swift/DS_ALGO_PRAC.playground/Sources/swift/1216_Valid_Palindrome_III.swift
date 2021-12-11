// Naive DFS with exhaustive search. TLE
class Solution {
    func isValidPalindrome(_ s: String, _ k: Int) -> Bool {
        guard s.count > k else {
            return true
        }
        return isValidPalindromeDFSHelper(Array(s), k)
    }
    
    func isValidPalindromeDFSHelper(_ sArray: [Character], _ k: Int) -> Bool {
        guard sArray.count > 1 else {
            return true
        }
        
        if isPalindrome(sArray) {
            return true
        } else if k > 0 {
            var result = [Bool]()
            for index in 0..<sArray.count {
                var isPalin = false
                if index == 0 {
                    isPalin = isValidPalindromeDFSHelper(Array(sArray[(index + 1)..<sArray.count]), k - 1)
                } else if index == sArray.count - 1 {
                    isPalin = isValidPalindromeDFSHelper(Array(sArray[0..<index]), k - 1)
                } else {
                    isPalin = isValidPalindromeDFSHelper(Array(sArray[0..<index]) + Array(sArray[(index + 1)..<sArray.count]), k - 1)
                }
                result.append(isPalin)
            }
            return !result.allSatisfy { $0 == false }
        } else {
            return false
        }
    }
    
    func isPalindrome(_ sArray: [Character]) -> Bool {
        var leftPtr = 0, rightPtr = sArray.count - 1
        while leftPtr <= rightPtr {
            if sArray[leftPtr] == sArray[rightPtr] {
                leftPtr += 1
                rightPtr -= 1
            } else {
                return false
            }
        }
        return true
    }
}

// 2D DP like Longest palindrome subsequence. Accepted
class Solution {
    func isValidPalindrome(_ s: String, _ k: Int) -> Bool {
        guard s.count > k else {
            return true
        }
        let sArray = Array(s)
        var dp = Array(repeating: Array(repeating: 0, count: sArray.count), count: sArray.count)
        
        for i in 0..<sArray.count {
            dp[i][i] = 1
        }
        
        for startIndex in stride(from: sArray.count - 2, through: 0, by: -1) {
            for endIndex in (startIndex + 1)..<sArray.count {
                if sArray[startIndex] == sArray[endIndex] {
                    dp[startIndex][endIndex] = 2 + dp[startIndex + 1][endIndex - 1]
                } else {
                    dp[startIndex][endIndex] = max(dp[startIndex + 1][endIndex], dp[startIndex][endIndex - 1])
                }
            }
        }
        
        return (sArray.count - dp[0][sArray.count - 1]) <= k
    }
}
