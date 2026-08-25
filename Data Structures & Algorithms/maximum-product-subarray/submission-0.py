class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # need to keep track of both current (subarray of eveerything before current num) min and max because of negatives
        sol = max(nums)
        currMin, currMax = 1, 1

        for n in nums:
            if n == 0:
                currMin, currMax = 1, 1
                continue
            
            temp = currMax * n
            currMax = max(n*currMax, n * currMin, n)
            currMin = min(temp, n*currMin, n)
            sol = max(sol, currMax)
        
        return sol

