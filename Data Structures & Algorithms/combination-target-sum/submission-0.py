class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []
        nums.sort()

        def dfs(idx, combo, curr_sum):
            #print(idx, combo, curr_sum)
            if idx > len(nums):
                return
            
            if curr_sum > target:
                return
            elif curr_sum == target:
                sol.append(combo[:])
            else:
                for i in range(idx, len(nums)):
                    combo.append(nums[i])
                    curr_sum += nums[i]
                    dfs(i, combo, curr_sum)
                    combo.pop()
                    curr_sum -= nums[i]
        
        dfs(0, [], 0)
        return sol
                
            
            