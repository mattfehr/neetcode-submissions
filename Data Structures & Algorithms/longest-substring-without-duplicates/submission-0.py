class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        in_window = set()
        l, r = 0, 0
        sol = 0

        while r < len(s):
            #print("Curr:", s[l:r+1], sol)
            if s[r] not in in_window:
                in_window.add(s[r])
                r += 1
            else:
                while s[r] in in_window:
                    sol = max(sol, r-l)
                    in_window.remove(s[l])
                    l += 1
                #print("Removed:", s[l:r+1], sol)
                # in_window.add(s[r])
                # r += 1
            #print("New:", s[l:r+1], sol)

        sol = max(sol, r-l)
        return sol