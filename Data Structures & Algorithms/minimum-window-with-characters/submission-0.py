class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Base case check
        if not s or not t or len(s) < len(t):
            return ""
        
        # Track character frequencies needed from t
        target_counts = Counter(t)
        window_counts = defaultdict(int)
        
        # "formed" tracks how many unique characters meet their target frequency
        formed = 0
        required = len(target_counts)
        
        # Result tuple: (window_length, left_index, right_index)
        ans = (float("inf"), None, None)
        
        l = 0
        r = 0
        while r < len(s):
            char = s[r]
            window_counts[char] += 1
            
            # If current character frequency matches target frequency, increment formed
            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1
                
            # Contract the window from the left once a valid window is found
            while l <= r and formed == required:
                char_l = s[l]
                
                # Update our minimum window result
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                    
                # Discard the leftmost character to look for smaller windows
                window_counts[char_l] -= 1
                if char_l in target_counts and window_counts[char_l] < target_counts[char_l]:
                    formed -= 1
                    
                l += 1
            r += 1
                
        # Return empty string if no valid window was found
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]

