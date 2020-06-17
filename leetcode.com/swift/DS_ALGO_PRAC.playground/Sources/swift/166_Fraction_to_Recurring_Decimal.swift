import Foundation
class Solution {
    func fractionToDecimal(_ numerator: Int, _ denominator: Int) -> String {
        if numerator == 0 || denominator == 0 {
            return "0"
        }
        var nume = numerator
        var dnume = denominator
        
        var result = [String]()
        if nume*dnume < 0 {
            result.append("-")
        }
        nume = abs(nume)
        dnume = abs(dnume)
        result.append(String(nume/dnume))
        var reminder = Int(Double(nume).truncatingRemainder(dividingBy: Double(dnume)))
        if reminder == nil || reminder == 0 {
            return result.joined(separator: "")
        }
        
        result.append(".")
        var cacheDict = [Int:Int]()
        while reminder != 0 {
            if cacheDict[reminder] != nil {
                result.insert("(", at: cacheDict[reminder]!)
                result.append(")")
                break
            }
            cacheDict[reminder] = result.count
            var div = (reminder*10) / dnume
            reminder = Int(Double(reminder).truncatingRemainder(dividingBy: Double(dnume)))
            result.append(String(div))
        }
        return result.joined(separator: "")
    }
}
