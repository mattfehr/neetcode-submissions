class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        
        leftMax = [0] * n
        rightMax = [0] * n

        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i]) #check if theres a new highest left
        
        rightMax[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i]) #check if there is a new highest right
        
        #keep highests because they determine wall size

        res = 0
        for i in range(n):
            # trapped water at index is min(sides) - height[i]
            res += min(leftMax[i], rightMax[i]) - height[i]
        return res
        
