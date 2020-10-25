import Foundation

class Solution {
    func slowestKey(_ releaseTimes: [Int], _ keysPressed: String) -> Character {
        let keys = Array(keysPressed)
        var times = [Character: Int]()
        for i in 0..<keys.count {
            if i == 0 {
                times[keys[i], default: 0] = releaseTimes[i]
            } else {
                times[keys[i], default: 0] = releaseTimes[i] - releaseTimes[i - 1]
            }
        }
        
        var timeCharMap = [Int: Character]()
        for (key, value) in times {
            timeCharMap[value] = key
        }
        
        return timeCharMap[timeCharMap.keys.sorted().first]
    }
}
