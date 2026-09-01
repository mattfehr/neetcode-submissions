public class Solution {
    public bool WordBreak(string s, List<string> wordDict) {
        
        Dictionary<int, bool> memo = new();


        bool dfs(int i) {
            if (i == s.Length) return true;
            if (memo.ContainsKey(i)) {
                return memo[i];
            }

            foreach (string word in wordDict) {
                if (i+word.Length <= s.Length && s[i..(i+word.Length)] == word) {
                    if (dfs(i+word.Length)) {
                        memo[i] = true;
                        return true;
                    }
                }
            }

            memo[i] = false;
            return false;
        }

        return dfs(0);

    }
}
