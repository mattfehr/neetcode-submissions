class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded_string = "";
        for (string s: strs ) {
            encoded_string += to_string(s.size()) + "#" + s;
        }
        return encoded_string;

    }

    vector<string> decode(string s) {
        vector<string> decoded_string = {};
        int i = 0;
        while (i < s.size()) {
            string num = "";
            while (s[i] != '#') {
                num += s[i];
                i += 1;
            }
            i += 1;
            string str = "";
            for (int j=i; j < i+stoi(num); j++) {
                str += s[j];
            }

            decoded_string.push_back(str);
            i = i+stoi(num);
        }
        return decoded_string;
    }
};
