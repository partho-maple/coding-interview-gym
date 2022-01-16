import Foundation

class Solution {
    func simplifyPath(_ path: String) -> String {
        var stack = [String]()
        let pathComponent = path.split(separator: "/")
        for component in pathComponent {
            if component == "" || component == "." || (stack.isEmpty && component == "..") {
                continue
            }
            if component == ".." {
                stack.removeLast()
                continue
            }
            stack.append(String(component))
        }
        return stack.isEmpty ? "/" : stack.reduce("") { $0 + "/" + $1 }
    }
}
