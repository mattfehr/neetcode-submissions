class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums: number[]): number[][] {
        const sol: number[][] = [];
        nums = [...nums].sort((a, b) => a - b);

        for (let i = 0; i < nums.length-2; ++i) {
            if (i > 0 && nums[i] === nums[i-1]) {
                continue;
            } 
            if (nums[i] > 0) {
                break;
            }

            let target = -nums[i];
            let l = i+1, r = nums.length-1;
            while (l < r) {
                let curr_sum = nums[l]+nums[r];
                if (curr_sum < target) {
                    l++;
                } else if (curr_sum > target) {
                    r--;
                } else {
                    sol.push([nums[i], nums[l], nums[r]]);
                    l++;
                    r--;
                    while (l<r && nums[l] === nums[l-1]) {
                        l++;
                    }
                    while (l<r && nums[r] === nums[r+1]) {
                        r--;
                    }
                }
            }
        }
        return sol;
    }
}
