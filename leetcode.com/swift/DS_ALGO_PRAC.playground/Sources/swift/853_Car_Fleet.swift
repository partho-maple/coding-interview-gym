class Solution {
    func carFleet(_ target: Int, _ position: [Int], _ speed: [Int]) -> Int {
        var (positionSpeedMap, sortedPositions, fleetCount, timeLastCarReached) = ([Int:Int](), position.sorted { $0 > $1 }, 0, -Double.infinity)
        for i in 0..<position.count {
            positionSpeedMap[position[i]] = speed[i]
        }
        
        for carPosition in sortedPositions {
            let speed = positionSpeedMap[carPosition]!
            let arrivalTime = Double(target - carPosition) / Double(speed)
            if arrivalTime > timeLastCarReached {
                fleetCount += 1
                timeLastCarReached = arrivalTime
            }
        }
        
        return fleetCount
    }
}
