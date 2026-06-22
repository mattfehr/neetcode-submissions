public class Solution {
    public int LongestConsecutive(int[] nums) {
        if (nums is null || nums.Length == 0) return 0;

        HashSet<int> nums_set = new HashSet<int>(nums);
        // int max_sol = 1;
        // foreach (int n in nums_set) {
        //     if (!nums_set.Contains(n-1)) {
        //         int start = n;
        //         int sol = 1;
        //         while (nums_set.Contains(start+1)) {
        //             start++;
        //             sol++;
        //         }
        //         max_sol = max_sol > sol ? max_sol : sol;
        //     }
        // }
        // return max_sol;
        return nums_set
            .Where(n => !nums_set.Contains(n-1))
            .Select(starts => {
                int count = 1;
                while (nums_set.Contains(++starts)) count++;
                return count;
            })
            .Max();

    }
}
