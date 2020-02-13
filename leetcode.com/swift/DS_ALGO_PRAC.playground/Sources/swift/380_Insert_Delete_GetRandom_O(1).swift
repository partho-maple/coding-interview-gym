import Foundation


class RandomizedSet {
    var valueIdxMap = [Int:Int]()
    var valueList = [Int]()

    /** Initialize your data structure here. */
    init() {
        
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    func insert(_ val: Int) -> Bool {
        guard self.valueIdxMap[val] == nil else {
            return false
        }
        self.valueIdxMap[val] = self.valueList.count
        self.valueList.append(val)
        return true
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    func remove(_ val: Int) -> Bool {
        guard self.valueIdxMap[val] != nil else {
            return false
        }
        let idx = self.valueIdxMap[val]
        let lastVal = self.valueList.last
        self.valueList[idx!] = lastVal!
        self.valueIdxMap[lastVal!] = idx
        self.valueList.popLast()
        self.valueIdxMap.removeValue(forKey: val)
        return true
    }
    
    /** Get a random element from the set. */
    func getRandom() -> Int {
        var idx = Int.random(in: 0..<self.valueList.count)
        return self.valueList[idx]
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * let obj = RandomizedSet()
 * let ret_1: Bool = obj.insert(val)
 * let ret_2: Bool = obj.remove(val)
 * let ret_3: Int = obj.getRandom()
 */
