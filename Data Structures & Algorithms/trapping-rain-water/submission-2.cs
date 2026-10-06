public class Solution {
    public int Trap(int[] height) {
        if (height == null || height.Length == 0) {
            return 0;
        }

        //go outside in
        int l = 0, r = height.Length - 1;
        int leftMax = height[l];
        int rightMax = height[r];
        int res = 0;
        while (l < r) {
            //trapped water per column is shorter of the two walls - its own height
            if (leftMax < rightMax) {
                //you know there is a wall of rightMax somewhere on the right
                l++;
                leftMax = Math.Max(leftMax, height[l]);
                //but the leftmax wall could be in the back
                res += leftMax - height[l];
                //if the current spot is the new leftmax, add 0 because no left wall
            } else {
                r--;
                rightMax = Math.Max(rightMax, height[r]);
                res += rightMax - height[r];
            }
        }
        return res;
    }
}