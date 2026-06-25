class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights: number[]): number {
        let l = 0, r = heights.length-1, max_height = 0;
        while (l < r ) {
            const height: number = (r-l) * Math.min(heights[l], heights[r]);
            max_height = Math.max(max_height, height); 
            if (heights[l] < heights[r]) {
                l++;
            } else {
                r--;
            }
        }
        return max_height;
    }
}
