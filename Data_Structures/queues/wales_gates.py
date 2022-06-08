# multi srouce bfs (bredth fresh search)

from collections import deque

class Solution:
    def wallsAndGates(self,rooms):             # List[List[int]] -> None:
        ROWS, COLS = len(rooms), len(rooms[0])
        visited = set()
        q = deque()

        # helper
        def addRoom(r,c):
            if (r<0 or r== ROWS or c<0 or c==COLS or (r,c) in visited or rooms[r][c]== -1):
                return
            visited.add((r,c))
            q.append([r,c])

        # hovering on each element of grid, identifying Gates(0) and add to queue
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))

        # start BFS
        dist = 0
        while q:
            for i in range(len(q)):
                r,c  = q.popleft()

                rooms[r][c] = dist   

                # grid step increase...
                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)
            
            dist += 1


            # time complexity = O(mn), space complexity = O(mn)

