class Solution:
    def climbStairs(self, n: int) -> int:
        table = [0] * (n+1)
        table[n] = 1
        #print(table)

        for i in range(n-1, -1, -1):
            if i+1 <= n:
                table[i] += table[i+1] 
            if i+2 <= n:
                table[i] += table[i+2] 

        #print(table)
        
        return table[0]