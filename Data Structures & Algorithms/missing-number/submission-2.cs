public class Solution {
    public int MissingNumber(int[] nums) {
        int sol = nums.Length;

        for (int i=0; i < nums.Length; ++i) {
            sol ^= i ^ nums[i];
        }
        return sol;
    }
}
