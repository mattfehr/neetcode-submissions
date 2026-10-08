class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ALPHABET = "abcdefghijklmnopqrstuvwxyz"
        s1_counts = {}
        curr_count = {}
        for letter in ALPHABET:
            s1_counts[letter] = 0
            curr_count[letter] = 0
        for char in s1:
            s1_counts[char] += 1
        
        
        l, r = 0, 0
        if len(s1) > len(s2):
            return False
        
        while r < len(s1):
            curr_count[s2[r]] += 1
            r += 1
        
        r -= 1
        while r < len(s2):
            #print(r, curr_count)
            if curr_count == s1_counts:
                return True
            curr_count[s2[l]] -= 1
            l += 1
            r += 1
            if r >= len(s2):
                break
            curr_count[s2[r]] += 1
        
        return False