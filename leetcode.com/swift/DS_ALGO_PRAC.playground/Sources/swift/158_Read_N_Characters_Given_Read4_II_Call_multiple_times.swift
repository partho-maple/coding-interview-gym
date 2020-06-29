import Foundation
/**
 * The read4 API is defined in the parent class Reader4.
 *     func read4(_ buf: inout [Character]) -> Int;
 */

class Solution : Reader4 {
    var localBufferCache = [Character]()
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    func read(_ buf: inout [Character], _ n: Int) -> Int {
        if n <= 0 {
            return n
        }

        var needToRead = n
        while needToRead > 0 && localBufferCache.count > 0 {
            buf[n - needToRead] = localBufferCache.removeFirst()
            needToRead -= 1
            if needToRead == 0 {
                return n
            }
        }
        
        let times = Int(needToRead/4) + 1
        for i in 0..<times {
            var localBuf = [Character](repeating: "#", count: 4)
            let readCount = read4(&localBuf)
            for i in 0..<readCount {
                localBufferCache.append(localBuf[i])
            }

            while needToRead > 0 && localBufferCache.count > 0 {
                buf[n - needToRead] = localBufferCache.removeFirst()
                needToRead -= 1
                if needToRead == 0 {
                    return n
                }
            }
        }
        return n - needToRead
    }
}

