class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        seen = set()

        def dfs(r, c, curr, nxt_idx):
            if (r,c) in seen:
                return False

            if board[r][c] != word[nxt_idx]:
                return False

            seen.add((r,c))
            curr += board[r][c]
        
            if curr == word:
                return True

            #print(r, c, curr)

            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if nr < 0 or nc < 0 or nr >= len(board) or nc >= len(board[0]):
                    continue
                if dfs(nr, nc, curr, nxt_idx+1):
                    return True
            
            seen.remove((r,c))
            curr = curr[:-1]
            return False
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    seen = set()
                    if dfs(r, c, "", 0):
                        return True
        return False
            
            
