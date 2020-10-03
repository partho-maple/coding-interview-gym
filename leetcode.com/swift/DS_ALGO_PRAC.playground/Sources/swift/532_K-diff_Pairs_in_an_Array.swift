class Solution {
    func findPairs(_ nums: [Int], _ k: Int) -> Int {
        var counter = [Int:Int]()
        for num in nums {
            counter[num, default: 0] += 1
        }
        
        var result = 0
        for (key, value) in counter {
            if k == 0 {
                if value > 1 {
                    result += 1
                }
            } else if let count = counter[key + k] {
                result += 1
            }
        }
        return result
    }
}
