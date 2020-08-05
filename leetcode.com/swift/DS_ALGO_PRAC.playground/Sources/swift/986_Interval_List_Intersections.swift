// Brute force
// Time O((m+n)log(m+n)) | Space O(m+n)
class Solution {
    func intervalIntersection(_ A: [[Int]], _ B: [[Int]]) -> [[Int]] {
        var mergedIntervals = A + B
        guard mergedIntervals.count > 1 else {
            return mergedIntervals
        }
        mergedIntervals.sort(by: { $0[0] < $1[0] })
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


// Improved linear
// Time O(m+n) | Space O(1)
class Solution {
    func intervalIntersection(_ A: [[Int]], _ B: [[Int]]) -> [[Int]] {
        var intersactions = [[Int]]()
        var (aIdx, bIdx) = (0, 0)
        while aIdx < A.count && bIdx < B.count {
            let (aInterval, bInterval) = (A[aIdx], B[bIdx])
            if (aInterval[1] >= bInterval[0]) && (aInterval[0] <= bInterval[1]) {
                let intersection = [max(aInterval[0], bInterval[0]), min(aInterval[1], bInterval[1])]
                intersactions.append(intersection)
            }
            if aInterval[1] < bInterval[1] {
                aIdx += 1
            } else if aInterval[1] > bInterval[1] {
                bIdx += 1
            } else {
                aIdx += 1
                bIdx += 1
            }
        }
        return intersactions
    }
}
