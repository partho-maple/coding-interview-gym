// BFS
class Solution {
    func numOfMinutes(_ n: Int, _ headID: Int, _ manager: [Int], _ informTime: [Int]) -> Int {
        var graph = [Int:[Int]]()
        for i in 0..<n {
            let directManager = manager[i]
            if directManager == -1 {
                continue
            }
            graph[directManager, default: [Int]()].append(i)
        }
        var totalTime = 0
        var nodeQueue = [(headID, 0)]
        while !nodeQueue.isEmpty {
            var (currentManager, infoTime) = nodeQueue.removeFirst()
            totalTime = max(totalTime, infoTime)
            if let neighbours = graph[currentManager] {
                for neighbour in neighbours {
                    nodeQueue.append((neighbour, infoTime + informTime[currentManager]))
                }
            }
        }
        return totalTime
    }
}

// DFS
class Solution {
    func numOfMinutes(_ n: Int, _ headID: Int, _ manager: [Int], _ informTime: [Int]) -> Int {
        var graph = [Int:[Int]]()
        for i in 0..<n {
            let directManager = manager[i]
            if directManager == -1 {
                continue
            }
            graph[directManager, default: [Int]()].append(i)
        }
        var totalTime = 0
        numOfMinutesDFSHelper(graph, informTime, headID, informTime[headID], &totalTime)
        return totalTime
    }
    
    func numOfMinutesDFSHelper(_ graph: [Int:[Int]], _ informTime: [Int], _ currentManager: Int, _ currentTime: Int, _ maxTime: inout Int) {
        guard let decendent = graph[currentManager], decendent.count > 0 else {
            maxTime = max(maxTime, currentTime)
            return
        }
        
        for eachDecendent in decendent {
            numOfMinutesDFSHelper(graph, informTime, eachDecendent, currentTime + informTime[eachDecendent], &maxTime)
        }
    }
}


