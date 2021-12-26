class Solution {
    func findBuildings(_ heights: [Int]) -> [Int] {
        var result = [Int](), currentMaxHeight = Int.min
        for i in stride(from: heights.count - 1, through: 0, by: -1) {
            let currentHeight = heights[i]
            if currentHeight > currentMaxHeight {
                result.append(i)
                currentMaxHeight = currentHeight
            }
        }
        return result.reversed()
    }
}
