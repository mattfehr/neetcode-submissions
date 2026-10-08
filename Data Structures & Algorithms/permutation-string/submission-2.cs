public class Solution {
    public bool CheckInclusion(string s1, string s2) {
        if (s1.Length > s2.Length) {
            return false;
        }

        int[] s1_count = new int[26];
        int[] s2_count = new int[26];

        // Populate counts only up to s1.Length
        for (int i = 0; i < s1.Length; i++) {
            s1_count[s1[i] - 'a']++;
            s2_count[s2[i] - 'a']++;
        }

        int matches = 0;
        for (int i = 0; i < 26; ++i) {
            if (s1_count[i] == s2_count[i]) {
                matches++;
            }
        }

        int l = 0, r = s1.Length;
        while (r < s2.Length) {
            if (matches == 26) return true;

            int idx = s2[l] - 'a';
            s2_count[idx]--;
            if (s1_count[idx] == s2_count[idx]) {
                matches++;
            } else if (s1_count[idx] == s2_count[idx] + 1) {
                matches--;
            }
            l++;

            idx = s2[r] - 'a';
            s2_count[idx]++;
            if (s1_count[idx] == s2_count[idx]) {
                matches++;
            } else if (s1_count[idx] == s2_count[idx] - 1) {
                matches--;
            }
            r++;
        }
        return matches == 26;
    }
}
