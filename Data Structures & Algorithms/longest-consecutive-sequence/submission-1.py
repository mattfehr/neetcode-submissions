class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        #print(num_set)
        starts = set()
        for n in nums:
            if n-1 not in num_set:
                starts.add(n)
        #print(starts)
        max_sol = 1
        for s in starts:
            start = s
            sol = 1
            while start+1 in num_set:
                start += 1
                sol += 1
            max_sol = max(sol, max_sol)
        return max_sol
