public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int n = nums.Length;
        int[] sol = new int[n];
        Array.Fill(sol, 1);

        int prod = 1;
        for (int i = 0; i < nums.Length; ++i) {
            sol[i] = prod;
            prod *= nums[i];
        }
        //Console.WriteLine(string.Join(", ", sol));

        prod = 1;
        for (int i = nums.Length-1; i >= 0; --i) {
            sol[i] *= prod;
            prod *= nums[i];
        }
        return sol;
    }
}
