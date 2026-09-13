/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        map<int, int> mp; //track number of active meetings
        for (Interval interval : intervals) {
            int start = interval.start;
            int end = interval.end;
            mp[start]++;    //meeting started at this time
            mp[end]--;      //meeting ended at this time
        }
        //map instead of unordered map becasue already sorted

        int prev = 0; //number of ongoing meetings
        int sol = 0; //max number of simultaneous meetings

        //iterate through every time point in and update the current number of meetings
        for (auto& [key, value] : mp) {
            prev += value;  
            sol = max(sol, prev);
        }
        return sol;

    }
};
