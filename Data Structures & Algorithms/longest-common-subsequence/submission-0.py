class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # two pointers
        # if they match take it and move both forward
        # if they dont - explore both paths by only moving one forward
        
        memo = {}

        def dfs(i, j):
            # out of bounds indices
            if i >= len(text1) or j >= len(text2):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            
            if text1[i] == text2[j]:
                take_both = dfs(i+1, j+1)
                memo[(i,j)] = 1 + take_both
                return 1 + take_both
            else:
                best_of_one = max(dfs(i+1, j), dfs(i, j+1))
                memo[(i,j)] = best_of_one
                return best_of_one
        
        return dfs(0,0)
        