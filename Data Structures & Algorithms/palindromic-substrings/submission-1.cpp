class Solution {
public:
    int countSubstrings(string s) {
        int count = 0;
        int n = s.size();
        vector<vector<bool>> dp(n, vector<bool>(n, false));

        for (int l = n-1; l >= 0; --l) {
            for (int r = l; r < n; ++r) {
                if (s[l] == s[r] && (r - l <= 2 || dp[l+1][r-1])) {
                    count++;
                    dp[l][r] = true;
                }
            }
        }
        return count;
    }
};
