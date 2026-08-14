public class Solution { 
    public int Rob(int[] nums) { 
        int n = nums.Length; 
        if (n == 0) return 0; 
        if (n == 1) return nums[0]; 
        
        // Slice A: Skip the last house
        int max1 = rob_linear(nums, 0, n - 2); 
        // Slice B: Skip the first house
        int max2 = rob_linear(nums, 1, n - 1); 
        
        return Math.Max(max1, max2); 
    } 
    
    public int rob_linear(int[] nums, int start, int end) { 
        if (start > end) return 0; 
        int length = end - start + 1; 
        
        // Use an array instead of a List to support instant index assignment
        int[] dp = new int[length + 1]; 
        
        // Base case: first house available
        dp[1] = nums[start]; 
        
        // Fill the table iteratively
        for (int i = 2; i <= length; ++i) { 
            // Choice 1: Skip current house -> take dp[i-1] 
            // Choice 2: Rob current house -> take nums[current] + dp[i-2] 
            int current_house_val = nums[start + i - 1]; 
            dp[i] = Math.Max(dp[i - 1], current_house_val + dp[i - 2]); 
        } 
        
        return dp[length]; 
    } 
}
