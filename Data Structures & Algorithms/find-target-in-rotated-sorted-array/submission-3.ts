class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums: number[], target: number): number {
        let l = 0, r = nums.length-1, m = 0;

        while (l <= r) {
            m = Math.floor(l + (r-l)/2);
            if (target == nums[m]) return m;
            else if (nums[l] <= nums[m]) {
                if (nums[l] <= target && target < nums[m]) {
                    r = m-1;
                } else {
                    l = m+1;
                }
            } else {
                if (nums[m] < target && target <= nums[r]) {
                    l = m+1;
                } else {
                    r = m-1;
                }
            }
        }
        return -1;
    }
}
