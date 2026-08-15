class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
            
        dp = {}
        max_len = 1
        start = 0
        
        # Base cases: all substrings of length 1 are palindromes
        for i in range(n):
            dp[(i, i)] = True
            
        # Base cases: substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i+1]:
                dp[(i, i+1)] = True
                start = i
                max_len = 2
            else:
                dp[(i, i+1)] = False
                
        # Check lengths from 3 to n
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                # Current is a palindrome if outer match and inner is true
                if s[i] == s[j] and dp[(i+1, j-1)]:
                    dp[(i, j)] = True
                    if length > max_len:
                        start = i
                        max_len = length
                else:
                    dp[(i, j)] = False
                    
        return s[start : start + max_len]