// Source: https://tinyurl.com/y56j4p76
import Foundation
class Solution {
    func removeComments(_ source: [String]) -> [String] {
        
        var result = [String]()
        var lineBuffer = ""
        var block_comment_open = false
        
        for line in source {
            var curr_index = 0
            var line_arr = Array(line).map { String($0) }
            
            while curr_index < line_arr.count {

                let current_char = line_arr[curr_index]
                
                if current_char == "/" && curr_index + 1 < line_arr.count && line_arr[curr_index + 1] == "/" && block_comment_open == false {
                    curr_index = line_arr.count + 1
                } else if current_char == "/" && curr_index + 1 < line_arr.count && line_arr[curr_index + 1] == "*" && block_comment_open == false {
                    block_comment_open = true
                    curr_index += 2
                } else if current_char == "*" && curr_index + 1 < line_arr.count && line_arr[curr_index + 1] == "/" && block_comment_open == true {
                    block_comment_open = false
                    curr_index += 2
                } else if block_comment_open == false {
                    lineBuffer += current_char
                    curr_index += 1
                } else {
                    curr_index += 1
                }
            }
            
            if lineBuffer != "" && lineBuffer.isEmpty == false && block_comment_open == false {
                result.append(lineBuffer)
                lineBuffer = ""
            }
        }
        return result
    }
}
