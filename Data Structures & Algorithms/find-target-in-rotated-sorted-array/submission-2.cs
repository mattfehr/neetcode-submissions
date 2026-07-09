public class Solution {
    public int Search(int[] nums, int target) {
        int l = 0, r = nums.Length-1, m;
        while (l <= r) {
            m = l + (r-l)/2;
            if (target == nums[m]) return m;
            if (nums[l] <= nums[m]) {
                if (nums[l] <= target && target < nums[m]) {
                    r = m-1;
                } else {
                    l = m+1;
                }
            }
            else {
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
