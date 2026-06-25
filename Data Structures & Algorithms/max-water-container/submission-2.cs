public class Solution {
    public int MaxArea(int[] heights) {
        int l = 0, r = heights.Length-1, max_height = 0;
        while (l < r) {
            int height = (r-l) * Math.Min(heights[l], heights[r]);
            max_height = Math.Max(max_height, height);

            if (heights[l] < heights[r]) {
                l++;
            } else {
                r--;
            }
        }
        return max_height;
    }
}
