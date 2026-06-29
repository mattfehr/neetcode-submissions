public class Solution {
    public int CharacterReplacement(string s, int k) {
        Dictionary<char, int> counts = new();
        int max_count = 0, sol = 0, l = 0, r = 0;

        while (r < s.Length) {
            counts[s[r]] = counts.GetValueOrDefault(s[r], 0) + 1; 
            max_count = Math.Max(max_count, counts[s[r]]);

            if ((r-l+1) - max_count > k) {
                counts[s[l]]--;
                l++;
            }

            sol = Math.Max(sol, r-l+1);
            r++;
        }
        return sol;
    }
}
