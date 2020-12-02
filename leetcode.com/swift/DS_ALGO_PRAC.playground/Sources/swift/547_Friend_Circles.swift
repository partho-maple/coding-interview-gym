class Solution {
    func findCircleNum(_ M: [[Int]]) -> Int {
        var visited = Set<Int>()
        var circleCount = 0
        for i in 0..<M.count {
            if !visited.contains(i) {
                circleCount += 1
                DFS(M, &visited, i)
            }
        }
        return circleCount
    }
    
    func DFS(_  M: [[Int]], _ visited: inout Set<Int>, _ node: Int) {
        for (neighbor, friendValue) in M[node].enumerated() {
            if friendValue == 1 && !visited.contains(neighbor) {
                visited.insert(neighbor)
                DFS(M, &visited, neighbor)
            }
        }
    }
}
