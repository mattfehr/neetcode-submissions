class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = [] #for each index i, the nearest smaller bar on the left

        leftMost = [-1] * n #if the stack is empty, no smaller bar exists so left boundary is index -1
        for i in range(n):
            #if the current bar is shorter than the bar on top of the stack, pop until no loner true
            while stack and heights[stack[-1]] >= heights[i]: #creates a strictly increasing stack (when using the indices)
                stack.pop()
            # top of the stack becomes the left boundary
            if stack:
                leftMost[i] = stack[-1]
            stack.append(i)

        #repeat the same to find the nearest smaller bar on the right
        stack = []
        rightMost = [n] * n
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)


        #for each bar, expand between the boundaries and compute its max rectangle
        maxArea = 0
        for i in range(n):
            leftMost[i] += 1
            rightMost[i] -= 1
            maxArea = max(maxArea, heights[i] * (rightMost[i] - leftMost[i] + 1))
        return maxArea