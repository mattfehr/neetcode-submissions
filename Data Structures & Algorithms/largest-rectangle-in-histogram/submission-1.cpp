class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        // we want the widest area each bar can act as the shorted bar
        int maxArea = 0;
        stack<pair<int, int>> stack; // pair: (index, height) keep in increasing order, each bar stores the earliest index where that height can start

        for (int i = 0; i < heights.size(); i++) {
            int start = i;
            while (!stack.empty() && stack.top().second > heights[i]) {
                pair<int, int> top = stack.top();
                int index = top.first;
                int height = top.second;
                maxArea = max(maxArea, height * (i - index));
                start = index;
                stack.pop();
            }
            stack.push({ start, heights[i] });
        }

        while (!stack.empty()) {
            int index = stack.top().first;
            int height = stack.top().second;
            maxArea = max(maxArea, height * (static_cast<int>(heights.size()) - index));
            stack.pop();
        }
        return maxArea;
    }
};