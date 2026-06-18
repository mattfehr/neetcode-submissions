public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> s = new HashSet<int>(nums);
        return s.Count != nums.Length;
    }
}