class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0, ]
        while stack:
            roomIdx = stack.pop()
            for key in rooms[roomIdx]:
                if not seen[key]:
                    seen[key] = True
                    stack.append(key)
        return all(seen)
