import Foundation

class Solution {
    func numDecodings(_ s: String) -> Int {
        let sArray = Array(s)
        let sLen = sArray.count
        guard sLen > 0 else {
            return 0
        }
        var dp = Array(repeating: 0, count: sLen + 1)
        dp[0] = 1
        for i in 1..<dp.count {
            if String(sArray[i - 1]) != "0" {
                dp[i] = dp[i - 1]
            }
            if i != 1 && Int(String(sArray[i - 2..<i]))! < 27 && Int(String(sArray[i - 2..<i]))! > 09 {
                dp[i] += dp[i - 2]
            }
        }
        return dp.last!
    }
}
