public class Solution {
    public int Rob(int[] nums) {
        int rob1 = 0; // Max money skipping current
        int rob2 = 0; // Max money including current
        
        foreach (int n in nums) {
            int temp = Math.Max(n + rob1, rob2);
            rob1 = rob2;
            rob2 = temp;
        }
        
        return rob2;
    }
}
