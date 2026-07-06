class Solution:
    def findMin(self, nums: List[int]) -> int:
        #[3,4,5,6,7,1,2] --> go right because 6 > 2
        #[3,4,5,6,7,8,9] --> go left because 6 < 9
        
        #if youre bigger then the right most, the min is right

        #[5,6,7,1,2,3] --> at 2 then go left
        #[5,6,7,8,1]
        #[0,1,6,7]
        #[5,1,2,3,4] --> go left because on the small side

        #case 1: big side e

        l, r = 0, len(nums)-1
        n = len(nums)
        while l <= r:
            print(l,r)
            m = (l+r)//2
            if nums[(m-1)%n] >= nums[m] and nums[(m+1)%n] >= nums[m]:
                return nums[m]
            elif nums[m] > nums[r]:
                l = m+1
            # elif nums[m] > nums[l]:
            #     r = m-1
            else:
                r = m-1

