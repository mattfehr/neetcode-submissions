class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,8,48]
        # [6, 24, 48, 48]

        prod = 1
        mults = []
        for n in nums:
            mults.append(prod * n)
            prod *= n
        
        prod = 1
        reverse_mults = []
        for n in reversed(nums):
            reverse_mults.append(prod * n)
            prod *= n
        reverse_mults.reverse()
        
        #print(mults, reverse_mults)

        sol = []
        for i in range(len(nums)):
            left = mults[i-1] if i - 1 >= 0 else 1 
            right = reverse_mults[i+1] if i+1 < len(nums) else 1
            sol.append(left*right)
        return sol