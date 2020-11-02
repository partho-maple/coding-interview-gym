// TLE
 class Solution {
     func numOfBurgers(_ tomatoSlices: Int, _ cheeseSlices: Int) -> [Int] {
         let maxJumbo = min(tomatoSlices/4, cheeseSlices)
         for jumboCount in 0...maxJumbo {
             let remainingTomatos = tomatoSlices - jumboCount*4
             let remainingCheese = cheeseSlices - jumboCount*1
             if remainingTomatos % 2 == 0 && remainingTomatos / 2 == remainingCheese {
                 return [jumboCount, remainingTomatos / 2]
             }
         }
         return []
     }
 }

class Solution {
    func numOfBurgers(_ tomatoSlices: Int, _ cheeseSlices: Int) -> [Int] {
        if tomatoSlices == 0 && cheeseSlices == 0 {
            return [0,0]
        }
        
        let small = ((4 * cheeseSlices) - tomatoSlices)/2
        let jumbo = cheeseSlices - small
        if small > 0 && jumbo > 0 {
            return [jumbo, small]
        } else {
            return []
        }
    }
}
