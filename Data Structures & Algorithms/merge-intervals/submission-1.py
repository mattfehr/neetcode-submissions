class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sol = []

        heapq.heapify(intervals)
        
        l, r = 0, 0
        while len(intervals) >= 2:
            #print(intervals)
            left = heapq.heappop(intervals)
            right = heapq.heappop(intervals)
            #if the two intervals overlap --> merge
            if right[0] <= left[1]:
                start = min(left[0], right[0])
                end = max(left[1], right[1])
                heapq.heappush(intervals, [start,end])
            #if they dont add both
            else:
                sol.append(left)
                sol.append(right)
        #print(intervals)

        #if sol is empty, there is only one big intervla
        if not sol:
            right = heapq.heappop(intervals)
            sol.append(right)
            return sol
        
        #there are one or zero intervals left
        if intervals:
            right = heapq.heappop(intervals)
            #need to do the last comparison
            left = sol.pop()
            #print(left, right)
            if right[0] <= left[1]:
                start = min(left[0], right[0])
                end = max(left[1], right[1])
                sol.append([start, end])
            else:
                sol.append(left)
                sol.append(right)
            
        return sol

