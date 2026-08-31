class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_map<int, bool> memo;
        return dfs(0, s, wordDict, memo);
    }

    bool dfs(int i, string s, vector<string>& wordDict, unordered_map<int, bool> &memo) {
        if (i == s.size()) return true;
        if (memo.contains(i)) {
            return memo[i];
        }

        for (string word : wordDict) {
            if (i+word.size() <= s.size() && s.substr(i, word.size()) == word) {
                if (dfs(i+word.size(), s, wordDict, memo)) {
                    memo[i] = true;
                    return true;
                }
            }
        }

        memo[i] = false;
        return false;
    }
};
