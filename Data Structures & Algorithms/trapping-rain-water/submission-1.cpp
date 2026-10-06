class Solution {
public:
    int trap(vector<int>& height) {
        if (height.empty()) {
            return 0;
        }
        //calculte horizontally not vertically, layer by layer
        stack<int> stk; //stack stores indices
        int sol = 0;

        for (int i = 0; i < height.size(); ++i) {
            // when there is a bar taller than the one on the top of stack, there is a right wall for a container >= current floor
            while (!stk.empty() && height[i] >= height[stk.top()]) {
                //if the end of a container is found, start adding up trapped water
                int mid = height[stk.top()];    //the bottom height of container
                stk.pop();
                if (!stk.empty()) {
                    int right = height[i];
                    int left = height[stk.top()];
                    int h = min(right, left) - mid;
                    int w = i - stk.top() - 1;
                    sol += h * w;
                }
            }
            stk.push(i);
        }
        return sol;
    }
};
