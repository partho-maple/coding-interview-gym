# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        self.backtrack(robot, (0, 0), 0, directions, visited)

    def backtrack(self, robot, cell, currentDirection, directions, visited):
        visited.add(cell)
        robot.clean()
        # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
        for i in range(4):
            newDirection = (currentDirection + i) % 4
            newCell = (cell[0] + directions[newDirection][0], cell[1] + directions[newDirection][1])
            if not newCell in visited and robot.move():
                self.backtrack(robot, newCell, newDirection, directions, visited)
                self.goBack(robot)  # go back to the previous cell and on the same direction
            # turn the robot following chosen direction : clockwise
            robot.turnRight()

    def goBack(self, robot):
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()




