class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counts;
        for (int n : nums) {
            counts[n]++;
        }
        vector<pair<int, int>> vec(counts.begin(), counts.end());
        sort(vec.begin(), vec.end(), [](const pair<int,int>& a, const pair<int,int>& b) {
            return a.second > b.second;
        });
        vector<int> sol;
        for (int i = 0; i < k; ++i) {
            sol.push_back(vec[i].first);
        }
        return sol;
    }
};
