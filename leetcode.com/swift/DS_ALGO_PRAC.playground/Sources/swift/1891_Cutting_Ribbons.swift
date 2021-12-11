class Solution {
    func maxLength(_ ribbons: [Int], _ k: Int) -> Int {
        var start = 1, end = ribbons.max()!, sum = ribbons.reduce(0, +)
        if k > sum {
            return 0
        }
        while start <= end {
            let mid = start + ((end - start) / 2)
            if iSPossibleToCut(ribbons, k, mid) {
                start = mid + 1
            } else {
                end = mid - 1
            }
        }
        return start - 1
    }
    
    func iSPossibleToCut(_ ribbons: [Int], _ k: Int, _ targetLength: Int) -> Bool {
        var count = 0
        for ribbon in ribbons {
            count += (ribbon / targetLength)
        }
        return count >= k ? true : false
    }
}
