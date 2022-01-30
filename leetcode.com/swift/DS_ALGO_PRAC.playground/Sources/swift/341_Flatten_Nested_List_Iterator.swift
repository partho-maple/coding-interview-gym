/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public func isInteger() -> Bool
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     public func getInteger() -> Int
 *
 *     // Set this NestedInteger to hold a single integer.
 *     public func setInteger(value: Int)
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     public func add(elem: NestedInteger)
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     public func getList() -> [NestedInteger]
 * }
 */

class NestedIterator {

    var nestedListStack = [([NestedInteger], Int)]()

    init(_ nestedList: [NestedInteger]) {
        self.nestedListStack.append((nestedList, 0))
    }

    func next() -> Int {
        let (nestedList, currentIndex) = nestedListStack.removeLast()
        let result = nestedList[currentIndex].getInteger()
        nestedListStack.append((nestedList, currentIndex + 1))
        return result
    }

    func hasNext() -> Bool {
        while !nestedListStack.isEmpty {
            let (nestedList, currentIndex) = nestedListStack.last!
            if currentIndex >= nestedList.count {
                nestedListStack.removeLast()
            } else {
                if nestedList[currentIndex].isInteger() {
                    return true
                } else {
                    nestedListStack[nestedListStack.count - 1] = (nestedList, currentIndex + 1)
                    nestedListStack.append((nestedList[currentIndex].getList(), 0))
                }
            }
        }
        return false
    }
}

/**
 * Your NestedIterator object will be instantiated and called as such:
 * let obj = NestedIterator(nestedList)
 * let ret_1: Int = obj.next()
 * let ret_2: Bool = obj.hasNext()
 */
