
// Getting TLE for some test cases due to infinit loop. No idea what's going wrong here, though spent a lot of time to figure it out
import Foundation
class Solution {
    func minSpeedOnTime(_ dist: [Int], _ hour: Double) -> Int {
        var minSpeed = 1, maxSpeed = dist.max()!
        while minSpeed < maxSpeed {
            let midSpeed = ((minSpeed + (maxSpeed - minSpeed)) / 2) + 1
            let totalTime = getTotalTimeFor(midSpeed, dist, hour)
            if totalTime > hour {
                minSpeed = midSpeed + 1
            } else {
                maxSpeed = midSpeed
            }
        }
        return getTotalTimeFor(minSpeed, dist, hour) <= hour ? minSpeed : -1
    }
    
    func getTotalTimeFor(_ speed: Int, _ dist: [Int], _ hour: Double) -> Double {
        var totalTime = 0.0
        for distance in dist {
            let currentTime = Double(Double(distance)/Double(speed))
            if distance == dist.last! {
                totalTime += currentTime
            } else {
                totalTime += currentTime.rounded(.up)
            }
        }
        return totalTime
    }
}
