#include <queue>
#include <vector>

class MedianFinder {
private:
    std::priority_queue<int, std::vector<int>, std::greater<int>> bigs; // Min-heap
    std::priority_queue<int> smalls;                                    // Max-heap

public:
    MedianFinder() {
        // Elements are automatically initialized as empty heaps
    }
    
    void addNum(int num) {
        // first number
        if (smalls.empty()) {
            smalls.push(num);
        }
        // if number should go to smalls and equal sides
        else if (num < smalls.top() && smalls.size() == bigs.size()) {
            smalls.push(num);
        }
        // if number should go to bigs and equal sides
        else if (num >= smalls.top() && smalls.size() == bigs.size()) {
            bigs.push(num);
            int smallest_big = bigs.top();
            bigs.pop();
            smalls.push(smallest_big);
        }
        // if number should go to smalls and smalls is bigger
        else if (num < smalls.top() && smalls.size() > bigs.size()) {
            int biggest_small = smalls.top();
            smalls.pop();
            bigs.push(biggest_small);
            smalls.push(num);
        }
        // if number should go to bigs and smalls is bigger
        else if (num >= smalls.top() && smalls.size() > bigs.size()) {
            bigs.push(num);
        }
    }
    
    double findMedian() {
        if (smalls.size() == bigs.size()) {
            double biggest_small = smalls.top();
            double smallest_big = bigs.top();
            return (biggest_small + smallest_big) / 2.0;
        } else {
            return smalls.top();
        }
    }
};
