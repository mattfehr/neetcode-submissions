class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;
        for (string s : strs) {
            int counts[26] = {0};
            for (char c : s) {
                counts[c-'a'] += 1;
            }

            //make the key
            string key = "";
            for (int i = 0; i < 26; ++i) {
                key += char(i + 'a') + to_string(counts[i]);
            }
            //add to group
            groups[key].push_back(s);
            
        }

        //make output
        vector<vector<string>> sol;
        for (const auto& [key, value] : groups) {
            sol.push_back(value);
        }
        return sol;
    }
};
