class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        //when two intervals overlap, keeping the one with the smaller end time leaves more room for future intervals

        sort(intervals.begin(), intervals.end());
        int removes = 0;
        int prevEnd = intervals[0][1];
        
        for (int i = 1; i < intervals.size(); i++) {
            int start = intervals[i][0];
            int end = intervals[i][1];
            if (start < prevEnd) {
                prevEnd = min(prevEnd, end);    //keep the smaller one
                removes += 1; //remove the bigger one
            } else {
                prevEnd = end; // no overlap so new prevEnd
            }
        }

        return removes;
    }
};
