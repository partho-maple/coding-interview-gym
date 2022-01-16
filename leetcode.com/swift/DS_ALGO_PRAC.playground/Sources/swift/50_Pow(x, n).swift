import Foundation

// Video: https://www.youtube.com/watch?v=g9YQyYi4IQQ
class Solution {
    func myPow(_ x: Double, _ n: Int) -> Double {
        if n == 0 {
            return 1
        }
        if n < 0 {
            return 1 / myPow(x, -n)
        }
        let half = myPow(x, n/2)
        if n % 2 == 0 {
            return half * half
        } else {
            return x * half * half
        }
    }
}
