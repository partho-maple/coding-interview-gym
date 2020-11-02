import Foundation

// My solution during MOC. Wrong answer
class Solution {
    func canTransform(_ start: String, _ end: String) -> Bool {
        var start = Array(start)
        var end = Array(end)
        guard start.count == end.count else {
            return false
        }
        
        var start_ptr = 0
        while start_ptr < start.count {
            if start[start_ptr] != end[start_ptr] {
                if start_ptr + 1 < start.count && ((start[start_ptr] == "X" && start[start_ptr + 1] == "L") || (start[start_ptr] == "R" && start[start_ptr + 1] == "X")) {
                    start.swapAt(start_ptr, start_ptr + 1)
                    if start[start_ptr] == end[start_ptr] && start[start_ptr + 1] == end[start_ptr + 1] {
                        start_ptr += 1
                    } else {
                        return false
                    }
                } else {
                    return false
                }
            }
            start_ptr += 1
        }
        return true
    }
}

// Source: https://tinyurl.com/y6cfe8gy
// Accepted
class Solution {
    func canTransform(_ start: String, _ end: String) -> Bool {
        var startArray = Array(start)
        var endArray = Array(end)
        
        guard startArray.count == endArray.count else {
            return false
        }
        
        if start.replacingOccurrences(of: "X", with: "") != end.replacingOccurrences(of: "X", with: "") {
            return false
        }
        
        var (L_start, L_end) = ([Int](), [Int]())
        var (R_start, R_end) = ([Int](), [Int]())
        
        for i in 0..<startArray.count {
            if startArray[i] == "L" {
                L_start.append(i)
            }
            if endArray[i] == "L" {
                L_end.append(i)
            }
            
            if startArray[i] == "R" {
                R_start.append(i)
            }
            if endArray[i] == "R" {
                R_end.append(i)
            }
        }
        
        for (i, j) in zip(L_start, L_end) {
            if i < j {
                return false
            }
        }
        
        for (i, j) in zip(R_start, R_end) {
            if i > j {
                return false
            }
        }
        return true
    }
}
