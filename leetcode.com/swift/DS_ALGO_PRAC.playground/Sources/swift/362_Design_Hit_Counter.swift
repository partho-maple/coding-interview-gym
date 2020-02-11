import Foundation

class HitCounter {

    var timestampHitMap: [Int: Int] = [:]
    var timestamps: [Int] = Array()
    
    /** Initialize your data structure here. */
    init() {
        
    }
    
    /** Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). */
    func hit(_ timestamp: Int) {
        if timestamp < 1 {
            return
        }
        if self.timestamps.count < 1 || self.timestamps.last != timestamp {
            self.timestamps.append(timestamp)
        }
        self.timestampHitMap[timestamp, default: 0] += 1
    }
    
    /** Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). */
    func getHits(_ timestamp: Int) -> Int {
        var hitCount = 0
        var startIdx = 0
        for i in stride(from: self.timestamps.count - 1, to: -1, by: -1) {
            let startTime = self.timestamps[i]
            if timestamp - startTime < 300 {
                hitCount += self.timestampHitMap[startTime] ?? 0
                startIdx = i
            } else {
                if self.timestampHitMap[startTime] != nil {
                    self.timestampHitMap.removeValue(forKey: startTime)
                }
            }
        }
        self.timestamps = Array(self.timestamps[startIdx...])
        return hitCount
    }
}

/**
 * Your HitCounter object will be instantiated and called as such:
 * let obj = HitCounter()
 * obj.hit(timestamp)
 * let ret_2: Int = obj.getHits(timestamp)
 */
