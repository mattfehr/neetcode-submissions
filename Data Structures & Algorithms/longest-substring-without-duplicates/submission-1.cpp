class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<int> in_window = {};
        int l = 0, r = 0, sol = 0;

        while (r < s.size()) {
            if (!in_window.contains(s[r])) {
                in_window.insert(s[r]);
                r++;
            } else {
                sol = max(sol, r-l);
                while (in_window.contains(s[r])) {
                    in_window.erase(s[l]);
                    l++;
                }
            }
        }
        sol = max(sol, r-l);
        return sol;
    }
};
