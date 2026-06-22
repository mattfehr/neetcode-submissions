#include <ranges> // Required for std::views::reverse

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, 1);

        // 1. Calculate left products (Prefix)
        int left_prod = 1;
        for (int i = 0; i < n; ++i) {
            res[i] = left_prod;
            left_prod *= nums[i];
        }
        for (int num : res) {
            std::cout << num << " ";
        }
        //[1,1,2,8]

        // 2. Calculate right products (Suffix) and multiply
        int right_prod = 1;
        for (int i = n - 1; i >= 0; --i) {
            res[i] *= right_prod;
            right_prod *= nums[i];
        }
        

        return res;
    }
};
