public class Solution {
    public int LengthOfLongestSubstring(string s) {
        HashSet<int> in_window = new();
        int l = 0, r = 0, sol = 0;
        while (r < s.Length) {
            if (!in_window.Contains(s[r])) {
                in_window.Add(s[r]);
                r++;
            } else {
                sol = Math.Max(sol, r-l);
                while (in_window.Contains(s[r])) {
                    in_window.Remove(s[l]);
                    l++;
                }
            }
        }
        sol = Math.Max(sol, r-l);
        return sol;
    }
}
