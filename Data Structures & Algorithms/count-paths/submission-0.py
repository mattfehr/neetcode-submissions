class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        
        def dfs(r, c):
            # out of bounds, not a possible path
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0
            # reached the end, is a path
            if r == m-1 and c == n-1:
                return 1
            if (r,c) in dp:
                return dp[(r,c)]

            bottom = dfs(r+1, c)
            right = dfs(r, c+1)

            dp[(r,c)] = bottom + right
            return bottom + right
        
        return dfs(0,0)