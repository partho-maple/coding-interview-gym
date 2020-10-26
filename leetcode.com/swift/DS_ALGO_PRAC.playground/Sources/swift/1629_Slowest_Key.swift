import Foundation

class Solution {
    func slowestKey(_ releaseTimes: [Int], _ keysPressed: String) -> Character {
        let keys = Array(keysPressed)
        var (maxTime, maxTimeChar) = (releaseTimes.first!, keys.first!)
        for i in 1..<keys.count {
            let time = releaseTimes[i] - releaseTimes[i - 1]
            if time > maxTime || (time == maxTime && keys[i] > maxTimeChar) {
                maxTimeChar = keys[i]
                maxTime = time
            }
        }
        return maxTimeChar
    }
}
