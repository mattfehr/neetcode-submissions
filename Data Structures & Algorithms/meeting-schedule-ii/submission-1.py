"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        minHeap = []
        time = 0
        count = 0

        intervals.sort(key=lambda i: i.start)
        for i in range(len(intervals)):
            start, end = intervals[i].start, intervals[i].end
            time = start

            #try to find a room for them
            if minHeap:
                room = heapq.heappop(minHeap)
                #check if room is open
                if room <= start:
                    # add room with end time
                    heapq.heappush(minHeap, end)
                #need a room
                else:
                    heapq.heappush(minHeap, room)
                    heapq.heappush(minHeap, end)
                    count += 1
            #if there is no room, add one
            else:
                heapq.heappush(minHeap, end)
                count += 1
        return count
            