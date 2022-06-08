def dfs(grid, r, c):

    nr, nc = len(grid), len(grid[0])

    if (r<0 or c<0 or r>=nr, c >=nc, grid[r][c] == 'o'):
        return
    
    grid[r][c] = '0'
    dfs(grid, r-1, c)
    dfs(grid, r +1, c)
    dfs(grid, r ,c-1)
    dfs(grid, r, c+1)


def numIslands1(grid):
    num_island = 0
    if grid == None or len(grid) == 0:
        return 0

    nr = len(grid)
    nc = len(grid[0])

    for r in nr:
        for c in nc:
            if (grid[r][c] == '1'):
                num_island  +=1
                dfs(grid, r, c)
    
    return num_island


from collections import deque
# bfs/ dfs common...
def numIslands(grid):
    if not grid:
        return 0

    visited = set()
    island = 0
    ROWS, COLS = len(grid), len(grid[0])

    #bfs
    def bfs(r,c):
        q = deque()
        q.append((r,c))
        visited.add((r,c))

        while q:
            rows, cols = q.pop()
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr, dc in directions:
                r,c = rows + dr, cols + dc
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



grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

print(numIslands(grid))