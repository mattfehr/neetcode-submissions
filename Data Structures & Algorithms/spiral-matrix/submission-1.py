from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
            
        sol = []
        l, r = 0, len(matrix[0]) - 1
        t, b = 0, len(matrix) - 1
        
        # Changed to <= to handle single rows/columns and the exact center
        while l <= r and t <= b:
            # 1. Left to right
            for i in range(l, r + 1):
                sol.append(matrix[t][i])
            t += 1
            
            # 2. Top to bottom
            for i in range(t, b + 1): # Start at t (since t was already updated)
                sol.append(matrix[i][r])
            r -= 1
            
            # Critical check: verify boundaries haven't crossed after updating t and r
            if not (l <= r and t <= b):
                break
                
            # 3. Right to left
            for i in range(r, l - 1, -1): # Fixed string syntax and starting index
                sol.append(matrix[b][i])
            b -= 1
            
            # 4. Bottom to top
            for i in range(b, t - 1, -1): # Fixed string syntax and starting index
                sol.append(matrix[i][l])
            l += 1
            
        return sol
