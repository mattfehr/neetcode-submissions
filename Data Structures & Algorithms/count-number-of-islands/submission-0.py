class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(row, col):
            if grid[row][col] == "0":
                return
            
            grid[row][col] = "0"

            for dr, dc in dirs:
                nr, nc = row+dr, col+dc
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS:
                    continue

                dfs(nr, nc)
        
        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
        return count
                