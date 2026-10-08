from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Stores indices of elements in a decreasing order of their values
        q = deque() 
        sol = []
        
        for r in range(len(nums)):
            # 1. Remove indices that are out of the current sliding window
            if q and q[0] < r - k + 1:
                q.popleft()
            
            # 2. Remove smaller elements from the back because they can't be the max
            while q and nums[q[-1]] < nums[r]:
                q.pop()
                
            # 3. Add the current element's index
            q.append(r)
            
            # 4. Once the window reaches size k, the maximum is always at the front
            if r >= k - 1:
                sol.append(nums[q[0]])
                
        return sol
