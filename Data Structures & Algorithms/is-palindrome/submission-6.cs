public class Solution {
    public bool IsPalindrome(string s)
    {
        ReadOnlySpan<char> span = s.AsSpan();
        int l = 0, r = span.Length - 1;

        while (l < r)
        {
            while (l < r && !char.IsLetterOrDigit(span[l])) l++;
            while (l < r && !char.IsLetterOrDigit(span[r])) r--;

            if (char.ToLowerInvariant(span[l]) != char.ToLowerInvariant(span[r])) return false;
            
            l++;
            r--;
        }
        return true;
    }
}
