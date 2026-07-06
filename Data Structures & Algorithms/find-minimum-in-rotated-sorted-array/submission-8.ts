class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums: number[]): number {
        let n = nums.length, l = 0, r = n-1, m = 0;
        while (l <= r) {
            m = Math.floor(l + (r-l)/2);
            if (nums[m] <= nums[((m+1)%n+n)%n] && nums[m] <= nums[((m-1)%n+n)%n]) {
                return nums[m];
            } else if (nums[m] > nums[r]) {
                l = m+1;
            } else {
                r = m-1;
            }
        }
    }
}
