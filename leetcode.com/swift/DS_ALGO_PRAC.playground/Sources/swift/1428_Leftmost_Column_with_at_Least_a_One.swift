/**
 * // This is the BinaryMatrix's API interface.
 * // You should not implement it, or speculate about its implementation
 * public class BinaryMatrix {
 *     public func get(_ row: Int, _ col: Int) -> Int {}
 *     public func dimensions() -> [Int] {}
 * };
 */

class Solution {
    func leftMostColumnWithOne(_ binaryMatrix: BinaryMatrix) -> Int {
        let (rows, cols) = (binaryMatrix.dimensions()[0], binaryMatrix.dimensions()[1])
        var leftMostCol = Int.max
        for row in 0..<rows {
            var (leftCol, rightCol) = (0, cols - 1)
            while leftCol <= rightCol {
                let midCol: Int = leftCol + (rightCol - leftCol) / 2
                if binaryMatrix.get(row, midCol) == 1 {
                    leftMostCol = min(leftMostCol, midCol)
                    rightCol = midCol - 1
                } else {
                    leftCol = midCol + 1
                }
            }
        }
        return leftMostCol == Int.max ? -1 : leftMostCol
    }
}
