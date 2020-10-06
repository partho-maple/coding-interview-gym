/**
 * Definition for Employee.
 * public class Employee {
 *     public var id: Int
 *     public var importance: Int
 *     public var subordinates: [Int]
 *     public init(_ id: Int, _ importance: Int, _ subordinates: [Int]) {
 *         self.id = id
 *         self.importance = importance
 *         self.subordinates = subordinates
 *     }
 * }
 */

import Foundation
class Solution {
    func getImportance(_ employees: [Employee], _ id: Int) -> Int {
        var importance = 0
        var id_importance_map = [Int:Int]()
        var id_subordinates_map = [Int:Set<Int>]()

        for employee in employees {
            id_importance_map[employee.id] = employee.importance
            id_subordinates_map[employee.id] = Set<Int>(employee.subordinates)
        }
        
        var queue = [Int]()
        queue.append(id)
        var visited = Set<Int>()
        while !queue.isEmpty {
            let current_id = queue.removeFirst()
            importance += id_importance_map[current_id]!
            for subordinate in id_subordinates_map[current_id]! {
                if !visited.contains(subordinate) {
                    visited.insert(subordinate)
                    queue.append(subordinate)
                }
            }
        }
        
        return importance
    }
}
