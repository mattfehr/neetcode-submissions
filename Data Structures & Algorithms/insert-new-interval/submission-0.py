from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        l, r = 0, n-1
        insert_idx = n # default if start is bigger than all
        
        while l <= r:
            m = l + (r-l)//2
            
            # Check if it belongs after the last element
            if m == n - 1:
                if newInterval[0] > intervals[m][0]:
                    insert_idx = n
                    break
            
            # if smaller than m, then it needs to go left
            if newInterval[0] < intervals[m][0]:
                insert_idx = m  # Track potential spot
                r = m-1
            # if bigger than m+1, it needs to go right
            elif m+1 < n and newInterval[0] > intervals[m+1][0]:
                l = m+1
            # in the right spot (between m and m+1)
            else:
                insert_idx = m + 1  # FIX: Explicitly assign the correct spot before breaking
                break
                
        # insert it
        intervals.insert(insert_idx, newInterval)
        
        # pass to merge overlapping intervals
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
                
        return res
