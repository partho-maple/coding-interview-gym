// Optimized solution
import Foundation
class Solution {
    func tictactoe(_ moves: [[Int]]) -> String {
        let size = 3
        var (rows, cols) = (Array(repeating: 0, count: size), Array(repeating: 0, count: size))
        var (diagonal, skew_diagonal) = (0, 0)
        for (index, move) in moves.enumerated() {
            let (i, j) = (move[0], move[1])
            let sign = index % 2 == 0 ? 1 : -1
            rows[i] += sign
            cols[j] += sign
            if i == j {
                diagonal += sign
            }
            if i + j == size - 1 {
                skew_diagonal += sign
            }
            if abs(rows[i]) == size || abs(cols[j]) == size || abs(diagonal) == size || abs(skew_diagonal) == size {
                return sign == 1 ? "A" : "B"
            }
        }
        return moves.count == (size*size) ? "Draw" : "Pending"
    }
}



// Naive stupid solution
import Foundation
class Solution {
    enum Result: String, RawRepresentable {
        case Pending
        case Draw
        case A
        case B
    }
    
    func tictactoe(_ moves: [[Int]]) -> String {
        guard moves.count > 0, moves.count <= 9 else {
            return Result.Pending.rawValue
        }
        
        var grid = Array(repeating: Array(repeating: "#", count: 3), count: 3)
        var aMove = true
        for move in moves {
            let (i, j) = (move[0], move[1])
            if aMove {
                grid[i][j] = "X"
            } else {
                grid[i][j] = "O"
            }
            aMove.toggle()
        }
        var result: Result = Result.Pending
        
        // Checks first row
        if grid[0][0] == grid[0][1] && grid[0][1] == grid[0][2] {
            if grid[0][0] == "X" {
                if result == .Pending || result == .A {
                    result = .A
                } else if result == .B || result == .Draw {
                    return Result.Draw.rawValue
                }
            } else if grid[0][0] == "O" {
                if result == .Pending || result == .B {
                    result = .B
                } else if result == .A || result == .Draw {
                    return Result.Draw.rawValue
                }
            }
        }
        
        // Checks first col
        if grid[0][0] == grid[1][0] && grid[1][0] == grid[2][0] {
            if grid[0][0] == "X" {
                if result == .Pending || result == .A {
                    result = .A
                } else if result == .B || result == .Draw {
                    return Result.Draw.rawValue
                }
            } else if grid[0][0] == "O" {
                if result == .Pending || result == .B {
                    result = .B
                } else if result == .A || result == .Draw {
                    return Result.Draw.rawValue
                }
            }
        }
        
        // Checks diagonal
        if grid[0][0] == grid[1][1] && grid[1][1] == grid[2][2] {
            if grid[0][0] == "X" {
                if result == .Pending || result == .A {
                    result = .A
                } else if result == .B || result == .Draw {
                    return Result.Draw.rawValue
                }
            } else if grid[0][0] == "O" {
                if result == .Pending || result == .B {
                    result = .B
                } else if result == .A || result == .Draw {
                    return Result.Draw.rawValue
                }
            }
        }
        
        // Checks second col
        if grid[0][1] == grid[1][1] && grid[1][1] == grid[2][1] {
            if grid[1][1] == "X" {
                if result == .Pending || result == .A {
                    result = .A
                } else if result == .B || result == .Draw {
                    return Result.Draw.rawValue
                }
            } else if grid[1][1] == "O" {
                if result == .Pending || result == .B {
                    result = .B
                } else if result == .A || result == .Draw {
                    return Result.Draw.rawValue
                }
            }
        }
        
        // Checks third col
        if grid[0][2] == grid[1][2] && grid[1][2] == grid[2][2] {
            if grid[0][2] == "X" {
                if result == .Pending || result == .A {
                    result = .A
                } else if result == .B || result == .Draw {
                    return Result.Draw.rawValue
                }
            } else if grid[0][2] == "O" {
                if result == .Pending || result == .B {
                    result = .B
                } else if result == .A || result == .Draw {
                    return Result.Draw.rawValue
                }
            }
        }
        
        // Checks anti diagonal
        if grid[0][2] == grid[1][1] && grid[1][1] == grid[2][0] {
            if grid[0][2] == "X" {
                if result == .Pending || result == .A {
                    result = .A
                } else if result == .B || result == .Draw {
                    return Result.Draw.rawValue
                }
            } else if grid[0][2] == "O" {
                if result == .Pending || result == .B {
                    result = .B
                } else if result == .A || result == .Draw {
                    return Result.Draw.rawValue
                }
            }
        }
        
        // Checks second row
        if grid[1][0] == grid[1][1] && grid[1][1] == grid[1][2] {
            if grid[1][0] == "X" {
                if result == .Pending || result == .A {
                    result = .A
                } else if result == .B || result == .Draw {
                    return Result.Draw.rawValue
                }
            } else if grid[1][0] == "O" {
                if result == .Pending || result == .B {
                    result = .B
                } else if result == .A || result == .Draw {
                    return Result.Draw.rawValue
                }
            }
        }
        
        // Checks third row
        if grid[2][0] == grid[2][1] && grid[2][1] == grid[2][2] {
            if grid[2][0] == "X" {
                if result == .Pending || result == .A {
                    result = .A
                } else if result == .B || result == .Draw {
                    return Result.Draw.rawValue
                }
            } else if grid[2][0] == "O" {
                if result == .Pending || result == .B {
                    result = .B
                } else if result == .A || result == .Draw {
                    return Result.Draw.rawValue
                }
            }
        }
        
        if result == .A || result == .B {
            return result.rawValue
        } else {
            if  moves.count == 9 {
                return Result.Draw.rawValue
            } else {
                return Result.Pending.rawValue
            }
        }
    }
}
