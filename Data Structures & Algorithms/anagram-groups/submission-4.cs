public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, List<string>> groups = new();
        foreach (string s in strs) {
            int[] counts = new int[26]; 
            foreach (char c in s) {
                counts[c-'a'] += 1;
            }
            StringBuilder sb = new StringBuilder();
            for (int i=0; i < 26; ++i) {
                sb.Append((char)(i + 'a')).Append(counts[i]);
            }
            string key = sb.ToString();
            if (!groups.ContainsKey(key)) {
                groups[key] = new List<string>();
            }
            groups[key].Add(s);
        }
        List<List<string>> sol = new();
        foreach (var pair in groups) {
            sol.Add(pair.Value);
        }
        return sol;
    }
}
