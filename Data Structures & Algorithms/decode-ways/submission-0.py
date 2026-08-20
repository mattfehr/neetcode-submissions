class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        
        def dfs(i):
            if i == len(s):
                return 1 #reached the end
            if s[i] == "0":
                return 0 #invalid number leading with 0 or just is 0
            if i in dp:
                return dp[i]
            
            count = dfs(i+1) #take one number

            #take 2 if possible
            if i+1 <= len(s)-1 and int(s[i:i+2]) <= 26:
                count += dfs(i+2)
            
            dp[i] = count
            return count
        
        return dfs(0) if s else 0

            