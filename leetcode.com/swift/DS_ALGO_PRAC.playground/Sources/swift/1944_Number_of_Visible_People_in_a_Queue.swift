// Brute Force. Time: O(n^2). TLE
class Solution {
    func canSeePersonsCount(_ heights: [Int]) -> [Int] {
        var visible = Array(repeating: 0, count: heights.count)
        for index in 0..<heights.count - 1 {
            var currentMax = Int.min
            for index2 in (index + 1)..<heights.count {
                if heights[index] < heights[index2] {
                    visible[index] += 1
                    break
                } else if heights[index] > heights[index2] && heights[index2] > currentMax {
                    visible[index] += 1
                    currentMax = heights[index2]
                }
            }
        }
        return visible
    }
}

// Increasing monotonic stack. Time: O(n). Accepted. https://tinyurl.com/y598x5s3
class Solution {
    func canSeePersonsCount(_ heights: [Int]) -> [Int] {
        guard heights.count > 1 else {
            return [0]
        }
        var visible = Array(repeating: 0, count: heights.count), incMonoStack = [Int]()
        for index in stride(from: heights.count - 1, through: 0, by: -1) {
            while !incMonoStack.isEmpty && heights[index] > incMonoStack.last! {
                incMonoStack.removeLast()
                visible[index] += 1
            }
            if !incMonoStack.isEmpty {
                visible[index] += 1
            }
            incMonoStack.append(heights[index])
        }
        return visible
    }
}
