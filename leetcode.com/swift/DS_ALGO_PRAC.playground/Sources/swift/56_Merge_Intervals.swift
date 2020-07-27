import Foundation

class Solution {
    func merge(_ intervals: [[Int]]) -> [[Int]] {
        guard intervals.count > 1 else {
            return intervals
        }
        var sortedIntervals: [[Int]] = intervals.sorted { $0[0] < $1[0] } // Sort the intervals by start time
        print(sortedIntervals)
        var mergedIntervals = [[Int]]()
        mergedIntervals.append(sortedIntervals.first!)
        print(mergedIntervals)
        for index in 1..<sortedIntervals.count {
            var previousInterval = mergedIntervals.last!
            var currentInterval = sortedIntervals[index]
            if previousInterval[1] >= currentInterval[0] {
                mergedIntervals.popLast()
                mergedIntervals.append([min(previousInterval[0], currentInterval[0]), max(previousInterval[1], currentInterval[1])])
            } else {
                mergedIntervals.append(currentInterval)
            }
        }
        return mergedIntervals
    }
}
