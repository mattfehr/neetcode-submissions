class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sol = len(nums)

        for i in range(len(nums)):
            sol ^= i ^ nums[i] #putting every expected number (i from 0 to n) and every actual number in a giant XOR equation
            # a XOR a cancels itself
            # start with n becaue i only goes to n-1
            # a XOR 0 is a
        
        return sol