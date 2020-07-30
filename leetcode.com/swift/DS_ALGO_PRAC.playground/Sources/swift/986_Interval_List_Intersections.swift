// brute force
// Time O((m+n)log(m+n)) | Space O(m+n)
class Solution {
    func intervalIntersection(_ A: [[Int]], _ B: [[Int]]) -> [[Int]] {
        var mergedIntervals = A + B
        guard mergedIntervals.count > 1 else {
            return mergedIntervals
        }
        mergedIntervals.sort(by: { $0[0] < $1[0] })
        print(mergedIntervals)
        var intersections = [[Int]]()
        for i in 0..<(mergedIntervals.count - 1) {
            let currentInterval = mergedIntervals[i]
            let nextInterval = mergedIntervals[i + 1]
            if currentInterval[1] >= nextInterval[0] {
                let intersection = [max(currentInterval[0], nextInterval[0]), min(currentInterval[1], nextInterval[1])]
                intersections.append(intersection)
                mergedIntervals[i + 1] = [max(currentInterval[0], nextInterval[0]), max(currentInterval[1], nextInterval[1])]
            }
        }
        return intersections
    }
}




