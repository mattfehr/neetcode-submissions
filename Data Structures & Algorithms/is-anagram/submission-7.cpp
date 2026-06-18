class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> s_chars;
        for (char c : s) {
            s_chars[c] += 1;
        }
        unordered_map<char, int> t_chars;
        for (char c : t) {
            t_chars[c] += 1;
        }
        return s_chars == t_chars;
    }
};
