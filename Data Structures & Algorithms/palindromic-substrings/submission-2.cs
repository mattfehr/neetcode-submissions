public class Solution {
    public int CountSubstrings(string s) {
        int count = 0, n = s.Length;
        bool[,] dp = new bool[n, n];
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                dp[r, c] = false;
            }
        }
        
        for (int l = n-1; l >= 0; --l) {
            for (int r = l; r < n; ++r) {
                if (s[l] == s[r] && (r - l <= 2 || dp[l+1, r-1])) {
                    dp[l, r] = true;
                    count++;
                }
            }
        }
        return count;
    }
}
