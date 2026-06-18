from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = Counter(s)
        t_chars = Counter(t)
        return s_chars == t_chars
        for key in s_chars.keys():
            if s_chars[key] != t_chars[key]:
                return False
        return True