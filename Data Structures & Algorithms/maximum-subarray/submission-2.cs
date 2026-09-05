public class Solution {
    private int?[,] memo;

    public int MaxSubArray(int[] nums) {
        memo = new int?[nums.Length, 2];
        return Dfs(nums, 0, false);
    }

    private int Dfs(int[] nums, int i, bool flag) { //flag = whether a subarray has already started
        if (i == nums.Length-1) {
            return flag ? Math.Max(0, nums[i]) : nums[i];
        }
        int f = flag ? 1 : 0;
        if (memo[i, f].HasValue) return memo[i, f].Value;
        memo[i, f] = flag ? Math.Max(0, nums[i] + Dfs(nums, i + 1, true)) //take max of restarting or continueing if subarray started
                          : Math.Max(Dfs(nums, i + 1, false),
                                     nums[i] + Dfs(nums, i + 1, true));
                            //if subarray hasnt started take max of 
        return memo[i, f].Value;


    }
}
