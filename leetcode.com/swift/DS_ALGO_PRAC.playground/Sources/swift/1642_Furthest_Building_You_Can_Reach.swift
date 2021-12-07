import Foundation

// Min Heap
class Solution {
    func furthestBuilding(_ heights: [Int], _ bricks: Int, _ ladders: Int) -> Int {
        var currentLadderAllocationMinHeap = Heap<Int>(sort: <), currentBrickAllocation = 0 //SOURCE:   https://github.com/raywenderlich/swift-algorithm-club/blob/master/Heap/Heap.swift
        for index in 0..<heights.count - 1 {
            let currentHeight = heights[index], nextHeight = heights[index + 1], climb = nextHeight - currentHeight
            if climb <= 0 {
                continue
            }
            currentLadderAllocationMinHeap.insert(climb)
            if currentLadderAllocationMinHeap.count <= ladders {
                continue
            }
            let neededBricks = currentLadderAllocationMinHeap.remove()!
            currentBrickAllocation += neededBricks
            if currentBrickAllocation > bricks {
                return index
            }
        }
        return heights.count - 1
    }
}

