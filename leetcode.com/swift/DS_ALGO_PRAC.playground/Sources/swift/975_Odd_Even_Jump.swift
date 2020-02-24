import Foundation

class Solution {
    func oddEvenJumps(_ A: [Int]) -> Int {
        let aLen = A.count
        var nextHeigher = Array(repeating: 0, count: aLen)
        var nextLower = Array(repeating: 0, count: aLen)
        
        var stack: [Int] = Array()
        var aValWithIdxTupleArray: [(num:Int, index:Int)] = A.enumerated().map { (index, element) in return (element, index) }
        aValWithIdxTupleArray = aValWithIdxTupleArray.sorted(by: { $0.num < $1.num })
        for (element, index) in aValWithIdxTupleArray {
            while stack.count > 0 && stack.last < index {
                nextHeigher[stack.popLast()] = index
            }
            stack.append(index)
        }
        
        stack.removeAll()
        var negative_aValWithIdxTupleArray: [(num: Int, index: Int)] = A.enumerated().map( (index, element) in return ((-element), index) )
        negative_aValWithIdxTupleArray = negative_aValWithIdxTupleArray.sorted(by: { $0.num < $1.num} )
        for (element, index) in negative_aValWithIdxTupleArray {
            while stack.count > 0 && stack.last < index {
                nextLower[stack.popLast()] = index
            }
            stack.append(index)
        }
        
        var oddJumpToHeigher = Array(repeating: 0, count: aLen)  // Indicates whether we can reach to end index from the respective index or not if we start with a Odd jump
        var evenJumpTolower = Array(repeating: 0, count: aLen)   // Indicates whether we can reach to end index from the respective index or not if we start with a Even jump
        oddJumpToHeigher[aLen - 1] = 1
        evenJumpTolower[aLen - 1] = 1
        for i in (aLen - 1)...0 {
            oddJumpToHeigher[i] = evenJumpTolower[nextHeigher[i]]
            evenJumpTolower[i] = oddJumpToHeigher[nextLower[i]]
        }
        return oddJumpToHeigher.reduce(0, +)
    }
}
