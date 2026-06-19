class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        sorted_dict = dict(sorted(counts.items(), key = lambda item: item[1], reverse=True))
        sol = []
        #print(sorted_dict)
        for key, value in sorted_dict.items():
            sol.append(key)
        #print(sol)
        #print(sol[:k])
        return sol[:k]