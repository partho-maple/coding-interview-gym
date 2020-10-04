import Foundation

// Brute force. Time: O(2^k). TLE
class Solution {
    func maxScore(_ cardPoints: [Int], _ k: Int) -> Int {
        var maxPoint = 0
        maxScoreDFSHelper(cardPoints, k, 0, cardPoints.count - 1, 0, &maxPoint)
        return maxPoint
    }
    
    func maxScoreDFSHelper(_ cardPoints: [Int], _ k: Int, _ leftIndex: Int, _ rightIndex: Int, _ currentPoint: Int, _ maxPoint: inout Int) {
        if k <= 0 {
            maxPoint = max(maxPoint, currentPoint)
            return
        }
        maxScoreDFSHelper(cardPoints, k - 1, leftIndex + 1, rightIndex, currentPoint + cardPoints[leftIndex], &maxPoint)
        maxScoreDFSHelper(cardPoints, k - 1, leftIndex, rightIndex - 1, currentPoint + cardPoints[rightIndex], &maxPoint)
    }
}


//  Sliding window. Time: O(k)
import Foundation
class Solution {
    func maxScore(_ cardPoints: [Int], _ k: Int) -> Int {
        guard cardPoints.count > 0 else {
            return 0
        }
        var maxPoint = cardPoints[cardPoints.count - k..<cardPoints.count].reduce(0) { $0 + $1 }
        var currentPoint = maxPoint
        for i in 0..<k {
            currentPoint = currentPoint + cardPoints[i] - cardPoints[cardPoints.count - k + i]
            maxPoint = max(maxPoint, currentPoint)
        }
        return maxPoint
    }
}
