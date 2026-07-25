class MedianFinder:

    def __init__(self):
        self.bigs = []    # Min-heap for the larger half
        self.smalls = []  # Max-heap for the smaller half (stores negative numbers)

    def addNum(self, num: int) -> None:
        # first number
        if not self.smalls:
            heapq.heappush(self.smalls, -num)

        # if number should go to smalls and equal sides
        elif num < -self.smalls[0] and len(self.smalls) == len(self.bigs):
            heapq.heappush(self.smalls, -num)

        # if number should go to bigs and equal sides
        elif num >= -self.smalls[0] and len(self.smalls) == len(self.bigs):
            heapq.heappush(self.bigs, num)
            smallest_big = heapq.heappop(self.bigs)
            heapq.heappush(self.smalls, -smallest_big)

        # if number should go to smalls and smalls is bigger
        elif num < -self.smalls[0] and len(self.smalls) > len(self.bigs):
            biggest_small = -heapq.heappop(self.smalls)
            heapq.heappush(self.bigs, biggest_small)
            heapq.heappush(self.smalls, -num)

        # if number should go to bigs and smalls is bigger
        elif num >= -self.smalls[0] and len(self.smalls) > len(self.bigs):
            heapq.heappush(self.bigs, num)

    def findMedian(self) -> float:
        if len(self.smalls) == len(self.bigs):
            biggest_small = -self.smalls[0]
            smallest_big = self.bigs[0]
            return (biggest_small + smallest_big) /2 
        else:
            return -self.smalls[0]
        