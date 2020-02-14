import Foundation

class Solution {
    func canCompleteCircuit(_ gas: [Int], _ cost: [Int]) -> Int {
        let stationCount = gas.count
        var startingStation = 0, gasSurplus = 0, gasDeficit = 0
        for i in 0..<stationCount {
            var gasBalance = gas[i] - cost[i]
            if gasBalance + gasSurplus >= 0 {
                gasSurplus += gasBalance
            } else {
                startingStation = i + 1
                gasDeficit += (gasBalance + gasSurplus)
                gasSurplus = 0
            }
        }
        return (gasSurplus + gasDeficit >= 0) ? startingStation : -1
    }
}
