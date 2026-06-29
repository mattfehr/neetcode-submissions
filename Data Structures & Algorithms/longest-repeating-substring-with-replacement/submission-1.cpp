class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> counts;
        int max_count = 0;
        int sol = 0;
        int l = 0, r = 0;

        while (r < s.size()) {
            counts[s[r]]++;
            max_count = max(max_count, counts[s[r]]);

            if ((r-l+1) - max_count > k) {
                counts[s[l]]--;
                l++;
            }

            sol = max(sol, r-l+1);
            r++;
        }
        return sol;
    }
};
