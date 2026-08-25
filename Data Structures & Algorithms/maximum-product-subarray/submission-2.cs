public class Solution {
    public int MaxProduct(int[] nums) {
        int sol = nums.Max();
        int currMax = 1, currMin = 1;

        foreach (int n in nums) {
            if (n == 0) {
                currMax = 1;
                currMin = 1;
                continue;
            }

            int temp = currMax * n;
            currMax = Math.Max(temp, Math.Max(currMin * n, n)); 
            currMin = Math.Min(temp, Math.Min(currMin * n, n)); 
            sol = Math.Max(sol, currMax);
        }

        return sol;
    }
}
