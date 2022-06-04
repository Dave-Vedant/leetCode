from collections import deque


def numIsland(grid):
    
    if not grid:
        return 0
    ROWS, COLS = len(grid), len(grid[0])
    island = 0
    visited = set()
    # bfs
    def bfs(r,c):
        q = deque()
        visited.add((r,c))
        q.append((r,c))
        while q:
            row, col  = q.popleft()
            directions  = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr, dc in directions:
                r,c = row + dr, col + dc
                if r in range(ROWS) and c in range(COLS) and grid[r][c] == "1" and (r,c) not in visited:
                    q.append((r,c))
                    visited.add((r,c))
    # main
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "1" and (r,c) not in visited:
                bfs(r,c)
                island +=1
    return island



grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid1 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

output = numIsland(grid1)
print(output)