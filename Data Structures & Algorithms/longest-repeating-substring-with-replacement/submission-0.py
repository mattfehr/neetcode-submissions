class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        counts = {letter : 0 for letter in ALPHABET}
        l, r = 0, 0
        max_count = 0
        sol = 0

        while r < len(s):
            counts[s[r]] += 1
            max_count = max(max_count, counts[s[r]])

            if (r-l+1) - max_count > k: #replacements = window size - count of most freq char
                counts[s[l]] -= 1
                l += 1
                #shifting the current max window size, not necesarily finding a window with more replacements to give

            sol = max(sol, r-l+1)
            r += 1

        return sol
