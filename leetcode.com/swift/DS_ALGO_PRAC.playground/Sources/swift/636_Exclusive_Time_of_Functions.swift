import Foundation
class Solution {
    func exclusiveTime(_ n: Int, _ logs: [String]) -> [Int] {
        var funcTimeMap = Array(repeating: 0, count: n)
        var funcStack = [Int]()
        var prevTime = 0
        for log in logs {
            let logItem = log.split(separator: ":")
            let (funct, type, tim) = (Int(logItem[0]), logItem[1], Int(logItem[2]))
            guard let function = funct, let time = tim else {continue}
            if type == "start" {
                if funcStack.count > 0 {
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
