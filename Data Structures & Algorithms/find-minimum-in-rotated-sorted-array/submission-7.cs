public class Solution {
    public int FindMin(int[] nums) {
        int n = nums.Length, l = 0, r = n-1, m;
        while (l <= r) {
            m = l + (r-l)/2;
            //sometimes mod of a negative will return a negative - muy mal
            if (nums[m] <= nums[((m+1)%n+n)%n] && nums[m] <= nums[((m-1)%n+n)%n]) {
                return nums[m];
            } else if (nums[m] > nums[r]) {
                l = m+1;
            } else {
                r = m-1;
            }
        }
        return -1;
    }
}
