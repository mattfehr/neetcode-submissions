class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        pairs = []

        for i in range(len(nums)-2):
            #skip dupes
            if i > 0 and nums[i] == nums[i-1]:
                continue

            #if lowest number > 0 then impossible
            if nums[i] > 0:
                break

            target = -nums[i]
            l, r = i+1, len(nums)-1
            while l < r:
                curr_sum = nums[l] + nums[r]
                if curr_sum < target:
                    l += 1
                elif curr_sum > target:
                    r -= 1
                else:
                    pairs.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    #skip dupes 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return pairs
        
        
