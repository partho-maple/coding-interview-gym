import Foundation

class Solution {
    func isPossibleDivide(_ nums: [Int], _ k: Int) -> Bool {
        var counter: [Int:Int] = [:]
        nums.forEach { num in
            counter[num, default: 0] += 1
        }
        print(counter)
        let sortedKeys = counter.keys.sorted()
        for key in sortedKeys {
            if counter[key] ?? 0 > 0 {
                let minus = counter[key]
                for i in key..<(key + k) {
                    if counter[i] == nil || counter[i]! < minus! {
                        return false
                    }
                    counter[i]! -= minus!
                }
            }
        }
        return true
    }
}


/*
nums = [1,2,3,3,4,4,5,6], k = 4
counter = [
1:1
2:1
3:2
4:2
5:1
6:1
]

nums.sort

*/
