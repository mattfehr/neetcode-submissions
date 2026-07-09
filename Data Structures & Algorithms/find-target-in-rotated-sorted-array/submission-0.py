class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # case 1 : m < r --> everything between is smaller than r (increasing) [1,2,3,4,5]
        # case 2 : m > r --> minimum is between or is r [7,8,9,0,2] [2,3,4,5,1]
        # case 3 : l > m --> minimum is in between or is m [7, 0, 1, 2, 5] [5,7,0,1,2]
        # case 4 : l < m --> everything in between is bigger than l (increasing) [1,2,3,4,5]

        # find the rotation point

        #[1,2,3,4,5,6,7]
        #[8,9,4,5,7] t=8.5, m < r and m < l

        #[1,2,3,4,0] m > r and m > l

        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target:
                return m
            # m in left segment
            if nums[l] <= nums[m]:
                # target in left segment
                if nums[l] <= target and target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            # m in right segment
            elif nums[m] <= nums[r]:
                # target in right segment
                if nums[m] < target and target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
        return -1


    
