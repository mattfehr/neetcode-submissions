class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0, r = heights.size()-1, max_height = 0;
        while (l < r) {
            int height = (r-l) * min(heights[l], heights[r]);
            max_height = max(max_height, height);

            if (heights[l] < heights[r]) {
                l++;
            } else {
                r--;
            }
        }
        return max_height;
    }
};
