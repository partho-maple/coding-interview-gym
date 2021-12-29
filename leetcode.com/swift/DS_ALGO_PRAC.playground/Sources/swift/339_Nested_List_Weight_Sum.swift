import Foundation

/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public func isInteger() -> Bool
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     public func getInteger() -> Int
 *
 *     // Set this NestedInteger to hold a single integer.
 *     public func setInteger(value: Int)
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     public func add(elem: NestedInteger)
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     public func getList() -> [NestedInteger]
 * }
 */

// Old solution
class Solution {
    func depthSum(_ nestedList: [NestedInteger]) -> Int {
        var wrightSum = 0
        self.depthSumHelper(nestedList, 1, &wrightSum)
        return wrightSum
    }
    
    func depthSumHelper(_ nestedList: [NestedInteger], _ currentWeight: Int, _ wrightSum: inout Int) {
        guard nestedList.count > 0 else {return}
        for i in stride(from: 0, to: nestedList.count, by: 1) {
            let nestedElement = nestedList[i]
            if nestedElement.isInteger() {
                wrightSum += (nestedElement.getInteger() * currentWeight)
            } else {
                self.depthSumHelper(nestedElement.getList(), currentWeight + 1, &wrightSum)
            }
        }
    }
}



// New solution
class Solution {
    func depthSum(_ nestedList: [NestedInteger]) -> Int {
        return depthSumDFSHelper(nestedList, 1)
    }

    func depthSumDFSHelper(_ nestedList: [NestedInteger], _ currentDepth: Int) -> Int {
        var currentSum = 0
        for nInt in nestedList {
            if nInt.isInteger() {
                currentSum += (nInt.getInteger() * currentDepth)
            } else {
                currentSum += (depthSumDFSHelper(nInt.getList(), currentDepth + 1))
            }
        }
        return currentSum
    }
}
