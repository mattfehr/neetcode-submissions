public class Solution {

    public string Encode(IList<string> strs) {
        string encoded_string = "";
        foreach (string s in strs) {
            encoded_string += (s.Length).ToString() + '#' + s;
        }
        return encoded_string;
    }

    public List<string> Decode(string s) {
        List<string> decoded = new();
        int i = 0;
        while (i < s.Length) {
            string num = "";
            while (s[i] != '#') {
                num += s[i];
                i += 1;
            }
            i++;
            int length = int.Parse(num);
            string str = s[i..(i+length)];
            decoded.Add(str);
            i += length;
        }
        return decoded;
   }
}
