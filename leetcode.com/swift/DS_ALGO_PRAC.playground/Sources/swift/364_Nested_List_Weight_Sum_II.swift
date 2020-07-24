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
import Foundation

class Solution {
    func depthSumInverse(_ nestedList: [NestedInteger]) -> Int {
        var maxDepth = getMaxDepth(nestedList)
        let weightedSum = getWeightedSum(nestedList, maxDepth)
        return weightedSum
    }
    
    private func getMaxDepth(_ nestedList: [NestedInteger]) -> Int {
        var currentMaxDepth = 0
        for nestedInt in nestedList {
            if nestedInt.isInteger() {
                currentMaxDepth = max(currentMaxDepth, 1)
            } else {
                var currentDepth = getMaxDepth(nestedInt.getList())
                currentMaxDepth = max(currentMaxDepth, currentDepth + 1)
            }
        }
        return currentMaxDepth
    }
    
    private func getWeightedSum(_ nestedList: [NestedInteger], _ depth: Int) -> Int {
        var currentSum = 0
        for nestedInt in nestedList {
            if nestedInt.isInteger() {
                currentSum += nestedInt.getInteger() * depth
            } else {
                currentSum += getWeightedSum(nestedInt.getList(), depth - 1)
            }
        }
        return currentSum
    }
}
