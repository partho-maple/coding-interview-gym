// Naive solution. O(row*col). TLE
class Solution {
    func wordsTyping(_ sentence: [String], _ rows: Int, _ cols: Int) -> Int {
        var (count, currentWordIndex) = (0, 0)
        for _ in 0..<rows {
            var col = -1
            while col < cols {
                col += Array(sentence[currentWordIndex]).count
                if col < cols {
                    col += 1
                    currentWordIndex += 1
                    if currentWordIndex >= sentence.count {
                        currentWordIndex = 0
                        count += 1
                    }
                }
            }
        }
        return count
    }
}

// DP. O(row*sentenceCount)
class Solution {
    func wordsTyping(_ sentence: [String], _ rows: Int, _ cols: Int) -> Int {
        for word in sentence {
            if word.count > cols {
                return 0
            }
        }
        
        var memo = [Int:(Int, Int)]() // CurrentWordIndex: (SentenceCountInCurrentRow, StartingWordIndexOfNextRow)
        var (totalSentenceCount, currentRowStartWordIndex) = (0, 0)
        for _ in 0..<rows {
            if let (currentSentenceCount, nextRowStartWordIndex) = memo[currentRowStartWordIndex] {
                totalSentenceCount += currentSentenceCount
                currentRowStartWordIndex = nextRowStartWordIndex
            } else {
                var (currentCol, currentRowSentenceCount, currentIndex) = (0, 0, currentRowStartWordIndex)
                while currentCol < cols {
                    let wordLen = Array(sentence[currentIndex]).count
                    if currentCol + wordLen <= cols {
                        currentCol += (wordLen + 1)
                        currentIndex = (currentIndex + 1) % sentence.count
                        if currentIndex == 0 {
                            currentRowSentenceCount += 1
                        }
                    } else {
                        break
                    }
                }
                totalSentenceCount += currentRowSentenceCount
                memo[currentRowStartWordIndex] = (currentRowSentenceCount, currentIndex)
                currentRowStartWordIndex = currentIndex
            }
        }
        
        return totalSentenceCount
    }
}
