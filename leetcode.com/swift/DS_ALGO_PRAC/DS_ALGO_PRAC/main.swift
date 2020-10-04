import Foundation
class Solution {
    func alphabetBoardPath(_ target: String) -> String {

        let board_array = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
            .map { Array($0)
                .map { String($0) } }
        
        let target_array = Array(target)
            .map { String($0) }
        
        var current_target_index = 0
        var queue = [(Int, Int, String)]()
        var visitedSet = Set<String>()
        var result = ""
        
        queue.append((0, 0, ""))
        visitedSet.insert(board_array[0][0])
        
        while queue.isEmpty == false {
            var (row, col, path) = queue.removeFirst()
            
            if board_array[row][col] == target_array[current_target_index] {

                path += "!"
                current_target_index += 1
                visitedSet.removeAll()
                queue.removeAll()
                visitedSet.insert(board_array[row][col])
                queue.append((row, col, path))
                
                if current_target_index >= target_array.count {
                    result = path
                    break
                } else {
                    continue
                }
            }
            
            for neighbor in [ (-1,0,"U"), (0,1,"R"), (1,0,"D"), (0,-1,"L") ] {
                let (new_row, new_col, direction) = (row + neighbor.0, col + neighbor.1, neighbor.2)
                if new_row < board_array.count &&
                    new_row >= 0 &&
                    new_col < board_array[new_row].count &&
                    new_col >= 0 &&
                    !visitedSet.contains(board_array[new_row][new_col]) {
                        
                        visitedSet.insert(board_array[new_row][new_col])
                        queue.append((new_row, new_col, path + direction))
                }
            }
        }
        return result
    }
}



let solution = Solution()

let input = "code"
let output = solution.alphabetBoardPath(input)
print("Result: \(output)")
