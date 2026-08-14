class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: 
            return nums[0]
            
        # original linear House Robber logic
        def rob_linear(sub_nums):
            cache = {}
            def dfs(i):
                if i >= len(sub_nums):
                    return 0
                if i in cache:
                    return cache[i]
                
                cache[i] = max(sub_nums[i] + dfs(i + 2), dfs(i + 1))
                return cache[i]
            return dfs(0)
        
        # Scenario 1: Skip the last house (nums[0] to nums[n-2])
        # Scenario 2: Skip the first house (nums[1] to nums[n-1])
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

            

        