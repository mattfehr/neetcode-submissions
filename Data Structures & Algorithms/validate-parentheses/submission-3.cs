public class Solution {
    public bool IsValid(string s) {
        Dictionary<char, char> map = new Dictionary<char, char>{ 
            ['('] = ')', 
            ['{'] = '}', 
            ['['] = ']' 
        }; 
        
        Stack<char> st = new Stack<char>(); 
        
        foreach (char c in s) { 
            // 1. If it's an opening bracket, push its expected closing bracket onto the stack
            if (map.ContainsKey(c)) { 
                st.Push(map[c]); 
            } 
            // 2. If it's a closing bracket, it MUST match the top of the stack
            else { 
                if (st.Count == 0 || st.Pop() != c) { 
                    return false; 
                } 
            } 
        } 
        // 3. If the stack is empty, all brackets were perfectly matched
        return st.Count == 0; 
    }
}
