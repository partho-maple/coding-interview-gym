import Foundation

// Brute force solution. Time Limit Exceeded
class Solution {
    func arrangeCoins(_ n: Int) -> Int {
        if n == 0 {
            return 0
        }
        
        var (coins, steps) = (0, 0)
        for i in 1...n {
            coins += i
            if coins <= n {
                steps += 1
            }
        }
        return steps
    }
}


// Binary Search
import Foundation
class Solution {
    func arrangeCoins(_ n: Int) -> Int {
        var (left, right) = (0, n)
        while left <= right {
            var mid: Int = (left + right)/2
            var requiredCoing = (mid*(mid + 1)) / 2
            if requiredCoing == n {
                return mid
            }
            if requiredCoing > n {
                right = mid - 1
            } else {
                left = mid + 1
            }
        }
        return right
    }
}

/*
 logn
 
 1-1
 2-3
 3-6
 4-10
 5-15
 6-21
 7-28
 8-36
 9-45
 1+2+3+4+5+6 = k(k+1)/2
 
*/
