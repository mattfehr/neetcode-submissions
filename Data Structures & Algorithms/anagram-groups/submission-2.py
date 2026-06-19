class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1

            key = []
            for i in range(26):
                key.append(chr(ord('a')+i)+str(counts[i]))
            key = "".join(key)
            groups[key].append(s)

        #print(groups.items())
        sol = []
        for key, value in groups.items():
            sol.append(value)
        return sol