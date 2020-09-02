/**
 * The read4 API is defined in the parent class Reader4.
 *     func read4(_ buf4: inout [Character]) -> Int;
 */

// Appriach 1
class Solution : Reader4 {
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    func read(_ buf: inout [Character], _ n: Int) -> Int {
        guard n > 0 else {
            return 0
        }
        var (copiedChars, readChars) = (0, 4)
        var buf4: [Character] = ["c", "a", "t", "!"]
        
        while copiedChars < n && readChars == 4 {
            readChars = super.read4(&buf4)
            
            for i in 0..<readChars {
                if copiedChars == n {
                    return copiedChars
                }
                buf[copiedChars] = buf4[i]
                copiedChars += 1
            }
        }
        return copiedChars
    }
}

