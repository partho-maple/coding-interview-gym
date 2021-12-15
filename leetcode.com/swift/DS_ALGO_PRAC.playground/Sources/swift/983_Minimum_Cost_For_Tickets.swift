
// Main idea: https://tinyurl.com/yy63r8cy
class Solution {
    func mincostTickets(_ days: [Int], _ costs: [Int]) -> Int {
        var dp = Array(repeating: 0, count: 396) // 365 + 31
        var daysSet = Set<Int>()
        for day in days {
            daysSet.insert(day)
        }
        
        for i in 31...395 {
            if !daysSet.contains(i - 30) {
                dp[i] = dp[i - 1]
            } else {
                dp[i] = [(dp[i - 1] + costs[0]), (dp[i - 7] + costs[1]), (dp[i - 30] + costs[2])].min()!
            }
        }
        return dp.last!
    }
}

// Main idea: https://tinyurl.com/yy63r8cy
class Solution {
    func mincostTickets(_ days: [Int], _ costs: [Int]) -> Int {
        var minCost = 0, last7daysQueue = [(Int, Int)](), last30daysQueue = [(Int, Int)]() // (day, cost) tuple
        for day in days {
            while !last7daysQueue.isEmpty && (last7daysQueue.first!.0 + 7) <= day {
                last7daysQueue.removeFirst()
            }
            while !last30daysQueue.isEmpty && (last30daysQueue.first!.0 + 30) <= day {
                last30daysQueue.removeFirst()
            }
            last7daysQueue.append((day, minCost + costs[1]))
            last30daysQueue.append((day, minCost + costs[2]))
            minCost = [minCost + costs.first!, last7daysQueue.first!.1, last30daysQueue.first!.1].min()!
        }
        return minCost
    }
}
