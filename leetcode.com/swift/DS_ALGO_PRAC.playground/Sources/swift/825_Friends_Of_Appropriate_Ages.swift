
// Brute force approach. Time: O(n^2)
// Time Limit Exceeded
import Foundation
class Solution {
    func numFriendRequests(_ ages: [Int]) -> Int {
        let contertedAges = ages.map {Double($0)}
        var existingRequestSet = Set<String>()
        for A in 0..<contertedAges.count {
            for B in 0..<contertedAges.count {
                if A == B {
                    continue
                }
                if contertedAges[B] <= (0.5 * contertedAges[A] + 7) {
                    continue
                }
                if contertedAges[B] > contertedAges[A] {
                    continue
                }
                if contertedAges[B] > 100 && contertedAges[A] < 100 {
                    continue
                }
                let requestKey = "\(A)-\(B)"
                if !existingRequestSet.contains(requestKey) {
                    existingRequestSet.insert(requestKey)
                }
            }
        }
        return existingRequestSet.count
    }
}


// Brute force approach. Time: O(1)
import Foundation
class Solution {
    func numFriendRequests(_ ages: [Int]) -> Int {
        let convertedAges = ages.map {Double($0)}
        var ageCount = [Double: Int]()
        for (index, item) in convertedAges.enumerated() {
            ageCount[item, default: 0] += 1
        }
        
        var requestSent = 0
        for (ageA, countA) in ageCount {
            for (ageB, countB) in ageCount {
                if ageB <= (0.5 * ageA + 7) {
                    continue
                }
                if ageB > ageA {
                    continue
                }
                if ageB > 100 && ageA < 100 {
                    continue
                }
                if ageA == ageB {
                    requestSent -= countA
                }
                requestSent += (countA * countB)
            }
        }
        return requestSent
    }
}
