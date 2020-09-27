import Foundation

class Solution {
    func angleClock(_ hour: Int, _ minutes: Int) -> Double {
        let (h, m) = (Double(hour), Double(minutes))
        var (hourPassed, minutesPassed) = (Double((30 * hour) % 360), Double((6 * minutes) % 360))
        let hourAdjustmanentForMinute = 0.5 * Double(minutes)
        hourPassed += hourAdjustmanentForMinute
                
        var diff: Double = 0
        if minutesPassed == hourPassed {
            return diff
        }
        diff = Double(abs(minutesPassed - hourPassed))
        return diff < Double(180) ? diff : Double(360 - diff)
    }
}
