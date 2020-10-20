import Foundation
class Solution {
    func compress(_ chars: inout [Character]) -> Int {
        guard chars.count > 0 else {
            return 0
        }
        
        var (rPtr, wPtr) = (0, 0)
        while rPtr < chars.count {
            var (prevChar, frequency) = (chars[rPtr], 0)
            while rPtr < chars.count && prevChar == chars[rPtr] {
                frequency += 1
                rPtr += 1
            }
            chars[wPtr] = prevChar
            wPtr += 1
            if frequency > 1 {
                for num in Array(String(frequency)) {
                    chars[wPtr] = num
                    wPtr += 1
                }
            }
        }
        return wPtr
    }
}
