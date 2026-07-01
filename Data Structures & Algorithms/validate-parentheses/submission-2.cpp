class Solution {
public:
    bool isValid(string s) {
        // Map closing brackets to opening brackets
        std::unordered_map<char, char> mapping = {
            {')', '('}, 
            {']', '['}, 
            {'}', '{'}
        };
        
        std::stack<char> st;
        
        for (char c : s) {
            // If it is a closing bracket
            if (mapping.count(c)) {
                if (st.empty() || st.top() != mapping[c]) {
                    return false;
                }
                st.pop();
            } else {
                // If it is an opening bracket
                st.push(c);
            }
        }
        
        return st.empty();
    }
};
