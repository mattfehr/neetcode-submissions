public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> diffs = new();
        for (int i=0; i < nums.Length; ++i) {
            int diff = target - nums[i];
            if (diffs.ContainsKey(diff)) return [diffs[diff], i];
            else diffs[nums[i]] = i;
        }
        return [];
    }
}
