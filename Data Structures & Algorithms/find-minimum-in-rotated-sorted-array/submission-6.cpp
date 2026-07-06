class Solution {
public:
    int findMin(vector<int> &nums) {
        int l = 0, r = nums.size()-1, m, n = nums.size();
        while (l <= r) {
            m = (l + (r-l) / 2); //no overflow
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
};
