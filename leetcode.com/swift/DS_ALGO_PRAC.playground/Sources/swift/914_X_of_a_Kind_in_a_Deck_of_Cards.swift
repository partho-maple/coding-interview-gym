import Foundation

// Brute force.
class Solution {
    func hasGroupsSizeX(_ deck: [Int]) -> Bool {
        guard deck.count > 1 else {
            return false
        }
        var cardCount = [Int: Int]()
        for card in deck {
            cardCount[card, default: 0] += 1
        }
        var N = deck.count
        for X in 2...N {
            var found = true
            
            for (key, value) in cardCount {
                if value % X != 0 {
                    found = false
                    break
                }
            }
            
            if found {
                return found
            }
        }
        return false
    }
}


// GCD
class Solution {
    func hasGroupsSizeX(_ deck: [Int]) -> Bool {
        guard deck.count > 1 else {
            return false
        }
        var cardCount = [Int: Int]()
        for card in deck {
            cardCount[card, default: 0] += 1
        }
        
        let gcdLocal = gcd(of: cardCount.values.sorted())
        return gcdLocal > 1 ? true : false
    }
    
    /// Euclid's algorithm to find GCD
    /// - Parameters:
    ///   - array: array to find cd for
    /// - Returns: gcd
    func gcd(of array: [Int]) -> Int {
        return array.reduce(0, gcd(_:_:))
    }
    
    
    /// Euclid's algorithm to find GCD
    /// - Parameters:
    ///   - a: larger integer
    ///   - b: smaller integer
    /// - Returns: gcd
    func gcd(_ a: Int, _ b: Int) -> Int {
        let r = a % b
        if r != 0 {
            return gcd(b, r)
        } else {
            return b
        }
    }
}
