public class Solution {
    public int UniquePaths(int m, int n) {

        Dictionary<(int, int), int> dp = new();
        
        int dfs(int r, int c) {
            if (r < 0 || r >= m || c < 0 || c >= n) {
                return 0;
            }
            if (r == m-1 && c == n-1) {
                return 1;
            }
            if (dp.ContainsKey((r,c))) return dp[(r,c)];

            int bottom = dfs(r+1, c);
            int right = dfs(r, c+1);

            dp[(r,c)] = bottom+right;
            return bottom + right;
        }

        return dfs(0,0);

    }
}
