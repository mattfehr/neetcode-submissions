class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        unordered_set<int> num_set(nums.begin(), nums.end());

        int max_sol = 1;
        for (int n : num_set) {
            if (!num_set.contains(n-1)) {
                int start = n;
                int sol = 1;
                while (num_set.contains(start+1)) {
                    start++;
                    sol++;
                }
                max_sol = max(max_sol, sol);
            }
        }
        return max_sol;
    }
};
