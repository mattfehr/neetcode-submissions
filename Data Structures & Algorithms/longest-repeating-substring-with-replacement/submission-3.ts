class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s: string, k: number): number {
        let max_count = 0, sol = 0, l = 0, r = 0;
        const counts = new Map<string, number>();

        while (r < s.length) {
            counts.set(s[r], (counts.get(s[r]) ?? 0) + 1);
            max_count = Math.max(max_count, counts.get(s[r])!);

            if ((r-l+1) - max_count > k) {
                counts.set(s[l], counts.get(s[l])! - 1);
                l++;
            }

            sol = Math.max(sol, r-l+1);
            r++;
        }
        return sol;
    }
}
