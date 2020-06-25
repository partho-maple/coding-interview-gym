import Foundation
class Solution {
    func exclusiveTime(_ n: Int, _ logs: [String]) -> [Int] {
        var funcTimeMap = Array(repeating: 0, count: n)
        var funcStack = [Int]()
        var prevTime = 0
        
        for log in logs {
            let logItem = log.split(separator: ":")
            let (functionOptional, type, timeOptional) = (Int(logItem[0]), logItem[1], Int(logItem[2]))
            guard let function = functionOptional, let time = timeOptional else {continue}
            
            // print("-----")
            // print("func: \(function), type: \(type), time: \(time), prevTime: \(prevTime)")
            // print(funcTimeMap)
            // print(funcStack)
            
            if type == "start" {
                if funcStack = funcStack.count > 0 {
                    funcTimeMap[funcStack.last!] += (time - prevTime)
                }
                prevTime = time
                funcStack.append(function)
            } else {
                funcTimeMap[funcStack.popLast()!] += (time - prevTime + 1)
                prevTime = time + 1
            }
        }
        return funcTimeMap
    }
}
