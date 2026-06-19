public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        Dictionary<int, int> counts = new Dictionary<int, int>();
        foreach (int n in nums) {
            counts[n] = counts.GetValueOrDefault(n, 0) + 1;
        }
        var sortedDict = counts.OrderByDescending(x => x.Value).Select(x => x.Key).Take(k).ToArray();;
        //int[] sol = sortedDict.Select(x => x.Key).Take(k).ToArray();
        return sortedDict;
    }
}
