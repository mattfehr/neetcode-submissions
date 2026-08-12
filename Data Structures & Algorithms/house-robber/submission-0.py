class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        
        def dfs(idx):
            if idx > len(nums)-1:
                return 0
            
            if idx in cache:
                return cache[idx]
            
            cache[idx] = max(nums[idx] + dfs(idx+2), dfs(idx+1))
            return cache[idx]
        
        return dfs(0)
