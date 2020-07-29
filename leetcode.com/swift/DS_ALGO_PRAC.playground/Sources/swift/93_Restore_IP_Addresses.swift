import Foundation

import Foundation

class Solution {
    func restoreIpAddresses(_ s: String) -> [String] {
        let digits: [Int] = Array(s).compactMap { $0.wholeNumberValue }
        guard digits.count >= 4 else {
            return []
        }
        
        var allAdress = [String]()
        restoreIpAddressesDFSHelper(digits, 0, [], &allAdress)
        return allAdress
    }
    
    private func restoreIpAddressesDFSHelper(_ digits: [Int], _ currentIdx: Int, _ currentAdress: [Int], _ allAdress: inout [String]) {
        if currentIdx >= digits.count && currentAdress.count == 4 {
            var currentAddrStr = currentAdress.map { String($0) }.joined(separator: ".")
            if currentAddrStr.count == digits.count + 3 {
                allAdress.append(currentAddrStr)
            }
            return
        }
        if currentAdress.count > 4 || currentIdx >= digits.count || (currentAdress.count >= 3 && (digits[currentIdx...].count > 3 || Int(digits[currentIdx...].map { String($0) }.reduce("", +))! > 255)) {
            return
        }
        var currentNum = 0
        for i in currentIdx..<min(currentIdx + 3, digits.count) {
            currentNum = currentNum*10 + digits[i]
            if currentNum >= 0 && currentNum <= 255 {
                restoreIpAddressesDFSHelper(digits, i + 1, currentAdress + [currentNum], &allAdress)
            } else {
                break
            }
        }
        return
    }
}
