class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # take or dont take

        #cache the results of previous index branches
        memo = {} # the state is index and the last number

        def dfs(i, last):
            #if at the end, no number to take or not take
            if i >= len(nums):
                return 0
            if (i, last) in memo:
                return memo[(i, last)]
            
            #take the number if its greater or dont
            if nums[i] > last:
                take = 1 + dfs(i+1, nums[i])
            else:
                take = 0

            dont_take = dfs(i+1, last)

            #take the best path
            memo[(i, last)] = max(take, dont_take)
            return memo[(i, last)]
        
        return dfs(0, -1001)