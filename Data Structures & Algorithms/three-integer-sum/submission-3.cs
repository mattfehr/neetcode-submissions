public class Solution {
    public List<List<int>> ThreeSum(int[] nums) {
        Array.Sort(nums);
        List<List<int>> sol = new();
        for (int i = 0; i < nums.Length-2; ++i) {
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }
            if (nums[i] > 0) break;

            int target = -nums[i];
            int l = i+1, r = nums.Length-1;
            while ( l < r ) {
                int curr_sum = nums[l] + nums[r];
                if (curr_sum < target) {l++;}
                else if (curr_sum > target) {r--;}
                else {
                    sol.Add([nums[i], nums[l], nums[r]]);
                    l++;
                    r--;
                    while (l<r && nums[l]==nums[l-1]) l++;
                    while (l<r && nums[r]==nums[r+1]) r--;
                }
            }
        }
        return sol;
    }
}
