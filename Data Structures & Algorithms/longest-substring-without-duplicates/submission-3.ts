class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s: string): number {
        const in_window = new Set<string>();
        let l = 0, r = 0, sol = 0;
        while (r < s.length) {
            if (!in_window.has(s[r])) {
                in_window.add(s[r]);
                r++;
            } else {
                sol = Math.max(sol, r-l);
                while (in_window.has(s[r])) {
                    in_window.delete(s[l]);
                    l++;
                }
            }
        }
        sol = Math.max(sol, r-l);
        return sol;
    }
}
