public class Solution {
    public int[][] Merge(int[][] intervals) {
        //basically keep track of all possible starts max end times


        // find the max start of all the intervals
        int max = 0;
        for (int i = 0; i < intervals.Length; ++i) {
            max = Math.Max(intervals[i][0], max);
        }

        //find the max end for every possible start
        int[] mp = new int[max+1];
        for (int i = 0; i < intervals.Length; i++) {
            int start = intervals[i][0];
            int end = intervals[i][1];
            mp[start] = Math.Max(end+1, mp[start]); //need +1 for valid time of 0
        }

        //complete the solution list using starts and max ends for merging
        var sol = new List<int[]>();
        int have = -1;
        int intervalStart = -1;
        for (int i = 0; i < mp.Length; ++i) {
            //skip starts that intervals never start with / dont have an end
            if (mp[i] != 0) {
                if (intervalStart == -1) {
                    intervalStart = i; //set interval start to current interval start
                }
                have = Math.Max(mp[i]-1, have); //max end we have
                //need -1 for the +1 used for valid 0 times
            }
            // if there is an end for the start, use that max end
            if (have == i) {
                sol.Add(new int[] {intervalStart, have});
                have = -1;
                intervalStart = -1;
            }
        }

        //account for last one if there is one for when the last merged interval ends exactly at the final index of mp
        if (intervalStart != -1) {
            sol.Add(new int[] {intervalStart, have});
        }

        return sol.ToArray();
    }
}
