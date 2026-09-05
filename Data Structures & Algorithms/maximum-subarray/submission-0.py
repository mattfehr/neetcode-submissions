class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # maximum sum of subarray ending at index i
        # at index i you can either take it or start a new subarray

        # base case: at the first element there is no history to look back on
        curr_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i]) #take past or start new
            max_sum = max(max_sum, curr_sum)
        return max_sum


